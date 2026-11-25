<!---
This file is used to generate your project datasheet.
-->

## How it works

A 640x480 @ 60 Hz VGA picture (25.175 MHz pixel clock, 2 bits per colour channel, TinyVGA Pmod
pinout) drawn with combinational logic from the pixel counters, no frame buffer. The design is
for the **micro tile** (`tiles: "micro"`: clk, rst_n, 8 inputs, 8 outputs, about 300 gates or 80
flip-flops); it is 34 flip-flops and about 260 gates (close to the limit, so there is no falling snow).

The picture is an 80 x 60 grid of 8-pixel cells:

- **Tree**: four stacked tiers of a fir tree (eight rows each, the half-width grows one cell a row
  and each tier starts two cells narrower than the last row of the tier above), darker green on
  the edge cells, striped needles, a brown trunk.
- **Star**: a diamond star on top that blinks through four colours (dark red, red, yellow, orange),
  a change about every 0.27 s.
- **Lights**: every fourth cell inside the tree is a light whose colour cycles
  (red, yellow, white, cyan) with the frame count.
- **Greeting**: the ground is snow, with **MALIGAYANG PASKO!** in red on it: 17 characters of a
  3x5-cell font (11 distinct glyphs) with a 5-cell-wide M, one cell between characters.
- Nothing is stored: the picture comes from the counters, a tier rule, a star rule, a glyph table
  and a few XORs.

`ui_in[0]` (PAUSE) freezes the frame counter, and with it the lights and the star.
The outputs are registered, so the picture is one clock late relative to the sync pulses.

The earlier 1x1 version of this project (full scene, `MERRY CHRISTMAS!` and `MALIGAYANG PASKO!` in an
8x8 font, 523 lines of Verilog) does not fit a micro tile; this version keeps the tree, the lights, the
star and the greeting in a smaller font.

## How to test

Connect a TinyVGA PMOD and a VGA monitor, apply a 25.175 MHz clock and release reset.
A Christmas tree with a blinking star and the greeting on the snow should appear.

## External hardware

TinyVGA PMOD (https://github.com/mole99/tiny-vga) and a VGA monitor.
