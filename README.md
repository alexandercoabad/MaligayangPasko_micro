![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Maligayang Pasko! A Christmas tree in a Tiny Tapeout micro tile

A 640x480 VGA pixel-art Christmas tree (compact blinking four-colour star, fuller four-tier fir tree with colour-cycling lights, falling snow in the night sky, and the greeting `MALIGAYANG PASKO!` in red on the snow, with a pause and three display options on the inputs) in the experimental sky130 **micro tile** (`tiles: "micro"` in info.yaml; clk, rst_n, 8 inputs, 8 outputs).

- [The datasheet](docs/info.md): how it works, the inputs, how to test it
- [src/project.v](src/project.v): the design, one file (34 flip-flops; hardened: 339 cells, 90.2 % utilisation, DRC and precheck clean)
- `src/config.json`, `src/no_synth.cells`: the micro-tile hardening settings (from the Ken Pettit's micro project, which fits the same tile)

## Inputs

All inputs low (or unconnected) gives the plain scene.

| Pin | Name | When high |
|-----|------|-----------|
| `ui[0]` | PAUSE | freezes the frame counter, and with it the snow, the lights and the star |
| `ui[1]` | SNOW_OFF | hides the falling snow |
| `ui[2]` | SKY_BLACK | black sky instead of dark blue |
| `ui[3]` | TEXT_GREEN | greeting in green instead of red |
| `ui[7:4]` | unused | |

The outputs are the TinyVGA Pmod pinout: `uo[0]` R1, `uo[1]` G1, `uo[2]` B1, `uo[3]` VSync, `uo[4]` R0, `uo[5]` G0, `uo[6]` B0, `uo[7]` HSync.

## VGA Playground



https://github.com/user-attachments/assets/e008854e-62fc-4536-b057-7bfacdb8a102



https://vga-playground.com/?repo=https://github.com/alexandercoabad/MaligayangPasko_micro

<img width="726" height="592" alt="Screenshot 2026-11-26 at 8 37 40 AM" src="https://github.com/user-attachments/assets/038d1ac4-4001-4011-b7f3-dca3e095231f" />

#3D viewer https://gds-viewer.tinytapeout.com/?model=https://alexandercoabad.github.io/MaligayangPasko_micro/tinytapeout.oas&pdk=sky130A
<img width="1048" height="663" alt="Screenshot 2026-11-26 at 9 26 37 AM" src="https://github.com/user-attachments/assets/49050208-c868-4f85-a79f-86cb0b5df5d9" />


## Simulation

```sh
cd test
make -B              # RTL: three frames against the cycle-exact model (test/model.py); writes frame.png
```

The test checks every clock of three frames against `test/model.py`, toggles the pause on the way, drives the three display options with a fixed pseudo-random pattern in the third frame, and measures the VGA timing from the sync pins. The same test runs on the gate-level netlist in the `gds` workflow (`gl_test`).

