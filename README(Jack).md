# python-median-prototype

Simplest working version of the Static Photo Generator.

Takes a video from a fixed camera, samples frames, and computes the
per-pixel median to remove moving people/objects.

## Run

```
pip install opencv-python numpy
python main.py your_video.mp4
```

Options: `--skip N` (keep 1 of every N frames), `--scale F` (resize factor),
`--out FILE` (output name, default `result.png`).

## Known limitations

- Camera must not move (use a tripod).
- A person who stays in one spot for most of the video will remain in the result.
- Long/high-res videos use a lot of memory; raise `--skip` or lower `--scale`.
