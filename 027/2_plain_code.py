def p(grid):
    """Add 2s to complete 180° rotational symmetry around a center.

    - Consider centers at integer or half-integer coordinates within the grid bounds.
    - For a given center (cy2,cx2) scaled by 2, rotate each 1 at (r,c) to (cy2-r, cx2-c).
      If the rotated partner is out of bounds -> center invalid.
      If the rotated partner is 0, we propose adding a 2 at that partner.
    - A center is valid only if all proposed additions lie on or to the left of the center
      (i.e., 2*col <= cx2).
    - Among valid centers, pick the one that yields the most additions (ties broken by
      smallest (cy2,cx2)).
    - Return the grid with the added 2s; original cells are unchanged.
    """

    h = len(grid)
    w = len(grid[0]) if h else 0
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    if not ones:
        return [row[:] for row in grid]

    best = None  # (missing_count, add_count, -cy2, -cx2, additions_set)

    # Only consider specified centers: (5.5,5.5)->(11,11) and (6,6)->(12,12)
    centers = [(9, 9), (10, 10)]
    for cy2, cx2 in centers:
            additions = set()
            missing = 0
            ok = True
            for r, c in ones:
                rr = cy2 - r
                cc = cx2 - c
                if not (0 <= rr < h and 0 <= cc < w):
                    ok = False
                    break
                if grid[rr][cc] == 0:
                    if 2 * cc <= cx2:
                        additions.add((rr, cc))
                    else:
                        missing += 1
            if not ok:
                continue
            score = (missing, len(additions), -cy2, -cx2)
            if best is None or score < best[:4]:
                best = (score[0], score[1], score[2], score[3], additions)

    # Apply best additions if any valid center found; otherwise leave grid unchanged
    out = [row[:] for row in grid]
    if best is not None:
        for r, c in best[4]:
            out[r][c] = 2
    return out
