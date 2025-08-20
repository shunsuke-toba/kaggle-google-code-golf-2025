# Task 198

You are given a grid containing only the value `0` and one other color `x`.
The `x` pixels form horizontal and vertical lines that make a rectangular
grid, but some cells on these lines may be missing and appear as `0`.
Each cell inside the grid is originally `0`.

Produce a new grid with the following rules:

- Pixels of color `x` remain `x`.
- Any `0` lying on a grid line (a row or column that contains mostly `x`) is
  changed to `4`.
- For each rectangle bordered by consecutive horizontal and vertical lines,
  fill all interior `0`s with:
  - `3` if all four bordering lines contain no `0`s.
  - `4` otherwise (i.e., if at least one side of the rectangle has a gap).

Return the transformed grid.
