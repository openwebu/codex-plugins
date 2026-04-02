---
name: "rembg"
description: "Use when the user wants to remove image backgrounds, generate transparent cutouts, or batch-process local assets with the rembg CLI."
---

# rembg

Use this skill for fast background removal from local images.

## Default workflow

1. Confirm input image path(s) and output location.
2. Ensure `rembg` is installed.
3. Run `rembg` with deterministic file-to-file commands.
4. Verify output files exist and report exact paths.

## Install (if missing)

```bash
python3 -m pip install --user rembg
```

If the command fails due to missing runtime libs, recommend installing system image dependencies and retrying.

## Single image

```bash
rembg i /absolute/path/input.jpg /absolute/path/output.png
```

Notes:
- Prefer `.png` output for transparency.
- Never overwrite original input unless user explicitly asks.

## Batch processing

```bash
mkdir -p /absolute/path/output
for f in /absolute/path/input/*.{png,jpg,jpeg,webp}; do
  [ -e "$f" ] || continue
  base="$(basename "${f%.*}")"
  rembg i "$f" "/absolute/path/output/${base}.png"
done
```

## Optional cleanup tuning (subject isolation)

```bash
rembg i -a /absolute/path/input.jpg /absolute/path/output.png
```

Use `-a` when the mask edge quality needs extra alpha matting.

## Output checklist

- Confirm each output file path.
- Confirm transparent background (PNG alpha).
- Report any failed files separately.
