# Task 260

We are given a rectangular grid of numbers. Exactly one diagonal line of a
non-zero colour different from **5** is present. The cells on this line have
constant value and form a straight line from the top-left to the bottom-right
(i.e. cells `(r,c)` with `r-c = k` for some constant `k`). All other cells are
`0` except possibly some **gray** cells valued `5`.

Treat the diagonal as a boundary splitting the grid into two triangular
regions: the **upper** region consists of cells with `r-c < k` (to the
upper‑right of the diagonal) and the **lower** region consists of cells with
`r-c > k` (to the lower‑left).

For each region independently:

- Remove all gray cells (`5`).
- If gray cells were present in that region, find their maximum distance from
  the diagonal, measured as `|r-c-k|`.
- Let `d` be this maximum distance. Draw a new diagonal of the original colour
  parallel to the existing one at a distance of `d+2` cells away: to the
  upper‑right side when dealing with the upper region, or to the lower‑left side
  when dealing with the lower region. Only cells that fall inside the grid are
  coloured.

The original diagonal remains unchanged in the output.
