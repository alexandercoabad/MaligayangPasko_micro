![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Maligayang Pasko! A Christmas tree in a Tiny Tapeout micro tile

A 640x480 VGA pixel-art Christmas tree (blinking four-colour star, colour-cycling lights, the greeting MALIGAYANG PASKO!) in the experimental sky130 **micro tile** (`tiles: "micro"` in info.yaml; clk, rst_n, 8 inputs, 8 outputs).

- [The datasheet](docs/info.md): how it works, the input, how to test it
- [src/project.v](src/project.v): the design, one file (34 flip-flops, about 260 gates)
- `src/config.json`, `src/no_synth.cells`: the micro-tile hardening settings (from the Pettit micro project, which fits the same tile)

## VGA Playground



https://github.com/user-attachments/assets/e008854e-62fc-4536-b057-7bfacdb8a102



https://vga-playground.com/?repo=https://github.com/alexandercoabad/MaligayangPasko_micro

<img width="726" height="592" alt="Screenshot 2026-11-26 at 8 37 40 AM" src="https://github.com/user-attachments/assets/038d1ac4-4001-4011-b7f3-dca3e095231f" />


## Simulation

```sh
cd test
make -B              # RTL: three frames against the cycle-exact model (test/model.py); writes frame.png
```

The 1x1 version of this project (full scene with the `MERRY CHRISTMAS!` / `MALIGAYANG PASKO!` banner and fonts) is in the git history.

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Set up your Verilog project

1. Add your Verilog files to the `src` folder.
2. Edit the [info.yaml](info.yaml) and update information about your project, paying special attention to the `source_files` and `top_module` properties. If you are upgrading an existing Tiny Tapeout project, check out our [online info.yaml migration tool](https://tinytapeout.github.io/tt-yaml-upgrade-tool/).
3. Edit [docs/info.md](docs/info.md) and add a description of your project.
4. Adapt the testbench to your design. See [test/README.md](test/README.md) for more information.

The GitHub action will automatically build the ASIC files using [LibreLane](https://www.zerotoasiccourse.com/terminology/librelane/).

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)

## What next?

- [Submit your design to the next shuttle](https://app.tinytapeout.com/).
- Edit [this README](README.md) and explain your design, how it works, and how to test it.
- Share your project on your social network of choice:
  - LinkedIn [#tinytapeout](https://www.linkedin.com/search/results/content/?keywords=%23tinytapeout) [@TinyTapeout](https://www.linkedin.com/company/100708654/)
  - Mastodon [#tinytapeout](https://chaos.social/tags/tinytapeout) [@matthewvenn](https://chaos.social/@matthewvenn)
  - X (formerly Twitter) [#tinytapeout](https://twitter.com/hashtag/tinytapeout) [@tinytapeout](https://twitter.com/tinytapeout)
  - Bluesky [@tinytapeout.com](https://bsky.app/profile/tinytapeout.com)
