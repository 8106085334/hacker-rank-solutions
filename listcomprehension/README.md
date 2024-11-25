# List Comprehension Challenge

This project solves a programming challenge using Python's list comprehension. The task generates all possible coordinate combinations `(i, j, k)` where the sum of `i + j + k` is not equal to a given value `n`.

## Problem Description

Given integers `x`, `y`, `z`, and `n`, the goal is to create a list of lists that contains all possible coordinates `[i, j, k]` such that:
- `0 <= i <= x`
- `0 <= j <= y`
- `0 <= k <= z`
- The sum of `i + j + k != n`

The solution uses Python's list comprehension for an efficient and compact implementation.

## Usage

To run the solution:
1. Clone this repository.
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
inputs:
x = 1
y = 1
z = 1
n = 2
output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]]
