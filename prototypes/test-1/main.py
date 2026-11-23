from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import numpy as np
from PIL import Image

image_dir = Path(__file__).resolve().parent.parent.parent / "test-images" / "set1"
extensions = {".jpg", ".jpeg", ".png", ".bmp"}


def load_flat_image(path: Path) -> np.ndarray:
    with Image.open(path) as img:
        # Only convert if not already RGB (avoids an unnecessary full-image copy)
        if img.mode != "RGB":
            img = img.convert("RGB")
        # np.array(..., copy=False) gets the buffer and flattens to 1D uint8
        return np.asarray(img).ravel()


paths = [
    p for p in image_dir.iterdir()
    if p.is_file() and p.suffix.lower() in extensions
]

# Parallel load -> returns a list of 1D NumPy arrays (one per file)
with ThreadPoolExecutor() as pool:
    per_file_1d: list[np.ndarray] = list(pool.map(load_flat_image, paths))

# Example fast processing per file using float32 (2x faster/smaller than float64)
scale = np.float32(1.0 / 255.0)
normalized_per_file = [arr * scale for arr in per_file_1d]
means_per_file = [arr.mean() for arr in per_file_1d]

# 1. Accumulate in float32 (avoids building a massive 2D float64 matrix in RAM)
accumulator = np.zeros_like(per_file_1d[0], dtype=np.float32)
for arr in per_file_1d:
    accumulator += arr

# Output: 1D array representing the average of all input images
average_image_1d = accumulator / len(per_file_1d)

with Image.open(paths[0]) as sample:
    width, height = sample.size

avg_rgb = average_image_1d.reshape((height, width, 3)).astype(np.uint8)
Image.fromarray(avg_rgb).save(image_dir / "result.png")