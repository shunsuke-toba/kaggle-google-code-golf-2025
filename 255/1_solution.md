# Task 255

You are given a 30×30 grid of integers. Cell value `0` represents black and any
other value is some other colour.

1. Find all axis-aligned rectangles of black cells whose width and height are
   at least `3`. A rectangle is valid only if the rectangle itself **and** a
   one‑cell border around it (clipped to the grid) contain only black cells.
   Choose among the valid rectangles the one with the largest longer side
   (`max(height,width)`), breaking ties by larger area. Recolour every cell in
   this rectangle with colour `3` (green).
2. Using the grid after step 1, examine each of the cells of this green
   rectangle. For each of the four directions (up, down, left, right) follow a
   ray starting from the neighbour in that direction. While moving along the
   ray, every traversed cell and the two cells immediately adjacent to the ray
   must be black (treat out‑of‑bounds as black). If the ray reaches the edge
   of the board under these conditions, colour every traversed cell green.

Return the resulting grid.
