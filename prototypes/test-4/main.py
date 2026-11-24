"""Median-based static photo generator (prototype).

Reads a video from a fixed camera, samples frames, and takes the per-pixel
median across frames. Moving objects (e.g. pedestrians) appear in any given
pixel only briefly, so the median keeps the real background.

Usage:
    python main.py test.mp4
    python main.py test.mp4 --skip 10 --scale 0.3 --out result.png
"""
import argparse
import cv2
import numpy as np


def read_frames(path, skip=5, scale=0.5):
    """Return a list of sampled, resized frames from the video."""
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video: {path}")
    frames, i = [], 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if i % skip == 0:
            frames.append(cv2.resize(frame, None, fx=scale, fy=scale))
        i += 1
    cap.release()
    print(f"Read {i} frames, kept {len(frames)}")
    return frames


def median_background(frames):
    """Per-pixel median over all frames -> one image without moving objects."""
    return np.median(np.stack(frames), axis=0).astype(np.uint8)


def main():
    parser = argparse.ArgumentParser(description="Remove moving objects from a video.")
    parser.add_argument("video", nargs="?", default="test.mp4")
    parser.add_argument("--skip", type=int, default=5, help="keep 1 of every N frames")
    parser.add_argument("--scale", type=float, default=0.5, help="resize factor")
    parser.add_argument("--out", default="result.png")
    args = parser.parse_args()

    frames = read_frames(args.video, args.skip, args.scale)
    if not frames:
        raise SystemExit("No frames were read.")
    cv2.imwrite(args.out, median_background(frames))
    print(f"Done! Saved {args.out}")


if __name__ == "__main__":
    main()
