from pathlib import Path
from PIL import Image
import numpy as np

# This script's own folder, and the example images it reads (shared with test-1)
here = Path(__file__).resolve().parent
image_dir = here.parent / "test-1"

# a = Image.open("1.png")
# print(a.size)

# names = []
# names.append("Tom")
# names.append("Amy")
# print(names)

# i = 3
# name = f"photo{i}.jpg"
# print(name)             # photo3.jpg

images = []
for i in range(1, 6):
    images.append(Image.open(image_dir / f"{i}.png").convert("RGB"))
print(len(images))

# arr = np.array(images[0])
# print(arr.shape)

arrays = []
for img in images:
    arrays.append(np.array(img))
stacked = np.stack(arrays)
print(stacked.shape)

result = np.mean(stacked, axis=0)
result = result.astype(np.uint8)
result = Image.fromarray(result)
result.save(here / "result_mean.png")
result = np.median(stacked, axis=0)
result = result.astype(np.uint8)
result = Image.fromarray(result)
result.save(here / "result.png")
