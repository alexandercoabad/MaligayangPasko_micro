# SPDX-FileCopyrightText: © 2026 Alexander Co Abad
# SPDX-License-Identifier: Apache-2.0
"""Every clock of a few frames against the cycle-exact model (model.py), with the pause input
toggled on the way, plus the VGA timing measured from the sync pins alone.  FRAMES=n in the
environment (default 3).  Frame 2 is written to frame.png when Pillow is installed."""

import os

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge

from model import Model

H_TOTAL, V_TOTAL = 800, 525


@cocotb.test()
async def test_video(dut):
    frames = int(os.environ.get("FRAMES", "3"))
    cocotb.start_soon(Clock(dut.clk, 40, unit="ns").start())   # 25 MHz

    dut.ui_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    await FallingEdge(dut.clk)
    dut.rst_n.value = 1

    model = Model()
    errors = 0
    hs_fall, vs_fall, hs_low, vs_low = [], [], 0, 0
    prev = 0xFF
    pic = {}
    for n in range(frames * H_TOTAL * V_TOTAL + 2 * H_TOTAL):
        # pause (ui_in[0]) is high for the last 20 lines of the second frame, so the frame counter skips one step
        line = n // H_TOTAL
        ui = 1 if (V_TOTAL + 505 <= line < 2 * V_TOTAL) else 0
        dut.ui_in.value = ui
        await FallingEdge(dut.clk)          # ui_in is seen by the next rising edge
        expect = model.step(ui)
        got = dut.uo_out.value
        if not got.is_resolvable or int(got) != expect:
            errors += 1
            if errors <= 10:
                dut._log.error(f"clock {n} (line {n // H_TOTAL % V_TOTAL}, col {n % H_TOTAL}): "
                               f"uo_out {got} expected {expect:08b}")
            continue
        got = int(got)
        if prev & 0x80 and not got & 0x80:
            hs_fall.append(n)
        if prev & 0x08 and not got & 0x08:
            vs_fall.append(n)
        hs_low += not got & 0x80
        vs_low += not got & 0x08
        prev = got
        f, c = divmod(n, H_TOTAL * V_TOTAL)
        if f == 1 and c % H_TOTAL < 640 and c // H_TOTAL < 480:
            pic[c] = got

    dut._log.info(f"{n + 1} clocks, {errors} mismatches, frame counter {model.t}")
    assert errors == 0
    # timing from the pins: 800 clocks a line with 96 of sync, 525 lines a frame with 2 of sync
    assert all(b - a == H_TOTAL for a, b in zip(hs_fall, hs_fall[1:]))
    assert all(b - a == H_TOTAL * V_TOTAL for a, b in zip(vs_fall, vs_fall[1:]))
    assert len(vs_fall) == frames
    assert hs_low == 96 * len(hs_fall)
    assert vs_low == 2 * H_TOTAL * len(vs_fall)
    # the picture is not blank: several colours are used
    assert len({v & 0x77 for v in pic.values()}) >= 6

    try:
        from PIL import Image
        im = Image.new("RGB", (640, 480))
        px = im.load()
        for c, v in pic.items():
            r, g, b = (v & 1) << 1 | (v >> 4) & 1, (v >> 1 & 1) << 1 | (v >> 5) & 1, (v >> 2 & 1) << 1 | (v >> 6) & 1
            px[c % H_TOTAL, c // H_TOTAL] = (r * 85, g * 85, b * 85)
        im.save("frame.png")
    except ImportError:
        pass
