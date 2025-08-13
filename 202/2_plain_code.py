def p(grid):
    """Propagate zeros across stripes depending on stripe orientation.

    Observation: Non-zero cells form uniform stripes either by rows (horizontal bands)
    or by columns (vertical bands). Zeros inside a band propagate orthogonally across
    the entire band if the two adjacent cells across the zero align with the band value.
    - Horizontal bands: if a zero has equal non-zero neighbors left and right (value v),
      set that column to 0 for all rows whose band value is v.
    - Vertical bands: if a zero has equal non-zero neighbors up and down (value v),
      set that row cells to 0 for all columns whose band value is v.
    """

    h = len(grid)
    w = len(grid[0]) if h else 0
    # Determine band orientation.
    def unique_nonzero(vals):
        s = {x for x in vals if x != 0}
        return s
    rows_ok = all(len(unique_nonzero(grid[r])) <= 1 for r in range(h))
    cols_ok = all(len(unique_nonzero(grid[r][c] for r in range(h))) <= 1 for c in range(w))

    # Build band maps
    if rows_ok and not cols_ok:
        orientation = 'h'
    elif cols_ok and not rows_ok:
        orientation = 'v'
    else:
        # Fall back: choose orientation with more lines that are uniform
        row_score = sum(1 for r in range(h) if len(unique_nonzero(grid[r])) <= 1)
        col_score = sum(1 for c in range(w) if len(unique_nonzero(grid[r][c] for r in range(h))) <= 1)
        orientation = 'h' if row_score >= col_score else 'v'

    out = [row[:] for row in grid]

    if orientation == 'h':
        # Map each row to its band value (first non-zero if any)
        row_val = []
        for r in range(h):
            v = 0
            for x in grid[r]:
                if x != 0:
                    v = x
                    break
            row_val.append(v)
        # For each zero, mark column per the row's band value
        cols_by_val = {}
        for r in range(h):
            vrow = row_val[r]
            if not vrow:
                continue
            for c in range(w):
                if grid[r][c] == 0:
                    cols_by_val.setdefault(vrow, set()).add(c)
        # Apply: for each value v, zero those columns for all rows whose band value is v
        for v, cols in cols_by_val.items():
            for r in range(h):
                if row_val[r] == v:
                    for c in cols:
                        out[r][c] = 0
    else:
        # Vertical bands: map each column to its band value (first non-zero in column)
        col_val = []
        for c in range(w):
            v = 0
            for r in range(h):
                if grid[r][c] != 0:
                    v = grid[r][c]
                    break
            col_val.append(v)
        # For each zero, mark the row per the column's band value
        rows_by_val = {}
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 0:
                    v = col_val[c]
                    if v:
                        rows_by_val.setdefault(v, set()).add(r)
        # Apply: for each value v, zero those rows for all columns whose band value is v
        for v, rows in rows_by_val.items():
            for c in range(w):
                if col_val[c] == v:
                    for r in rows:
                        out[r][c] = 0

    return out
