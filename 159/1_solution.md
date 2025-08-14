# Task 159

Given a grid, one colour forms a one-pixel thick square frame using the colour `2`. Somewhere else in the grid there is a small pattern made of colours other than `2` (and possibly `0`).

Let the frame's side length be `S`. The interior of the frame has size `S-2`, and this size is an integer multiple of the side length of the small pattern.

Crop the output to the square frame and fill its interior with a scaled copy of the small pattern so that it exactly covers the interior. Each cell of the pattern should be expanded into a block, keeping zeroes as zeroes. The border of the output remains colour `2`.

Return this `S×S` grid.
