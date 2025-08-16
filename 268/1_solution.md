# Task 268

We are given a grid containing `0` (black) and exactly one other colour `c`.
Cells of colour `c` form the border of an axis‑aligned rectangle, but some
border cells are missing (equal to `0`).

Perform the following:

1. Find the minimal rectangle containing all cells of colour `c`.
2. Recolour every cell inside this rectangle, including missing border cells,
   with the colour `4`.
3. For each missing border cell, paint additional cells with colour `4` outside
   the rectangle:
   - Colour a straight line of `4`s extending outward perpendicular to the
     border direction.
   - If the missing cell is at an end of its contiguous gap (i.e. its neighbour
     along the border is colour `c` or the rectangle corner), also colour a
     diagonal line of `4`s extending outward in that direction.
   - Lines continue until leaving the grid or hitting a non‑zero cell.

Return the resulting grid.
