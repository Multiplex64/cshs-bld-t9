# Median Background Prototype

Stacks the example images and takes the **median** of every pixel across all frames.

A moving object only covers a given pixel in a few frames, so the median picks the background color and the object disappears. An average (mean) would leave a faint "ghost" of the object instead; this script also saves the mean so the two can be compared.

## Input

Reads `1.png` to `5.png` from the [test-1](../test-1) folder (shared, so the large images aren't stored twice).

## Output

Saved next to this script (ignored by git):

- `result.png`: median of all frames (the clean background)
- `result_mean.png`: mean of all frames, for comparison

## Run

```
pip install -r requirements.txt
python median.py
```
