# Algorithm 1 README

## Overview / Description
This algorithm receives:
- `n`: the number of black (and white) disks in the list.
- `disks`: a list containing `'black'` or `'white'` alternating in order.

The algorithm organizes the disks so that **all black disks are on the left** and **all white disks are on the right**, using only adjacent swaps.

## Installation / Setup
Need:
- Python installed on your computer (any version ≥3.x).
- An IDE or online editor to run Python code.

## Usage / Examples
Call the `algo1()` function and pass:
- An integer `n` (number of black disks).
- A list of `2n` disks containing `'black'` and `'white'`.

Example:
```python
n = 4
disks = ['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black']
swaps, sorted_disks = algo1(n, disks)
print(swaps)
print(sorted_disks)
