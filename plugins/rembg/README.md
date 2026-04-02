# rembg

## Top Skills

- `rembg`

## What It Can Do

- Removes image backgrounds from local files using the `rembg` CLI workflow.
- Produces transparent PNG cutouts suitable for web, product, and marketing assets.
- Supports both one-off processing and batch background removal runs.

## Why Use It

- Speeds up asset preparation without leaving your terminal workflow.
- Makes transparent image generation repeatable and scriptable.
- Keeps original source files intact while writing clean outputs.

## How It Works

1. Ensures `rembg` is available.
2. Runs deterministic file-to-file commands on local images.
3. Verifies output paths and reports any failures.

## Quick Examples

```text
Use rembg to remove the background from ./assets/product.jpg and save it as ./assets/product-cutout.png.
```

```text
Batch-remove backgrounds from all images in ./raw-images and write PNG cutouts to ./clean-images.
```

## Requirements

- Python 3 and `pip` available locally.
- `rembg` installed (`python3 -m pip install --user rembg`).
- Local image file paths to process.
