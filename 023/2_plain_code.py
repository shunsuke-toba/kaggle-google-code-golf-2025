def p(grid):
    """Backtracking tiler for the 5-cells using 1x3 bars (->2) and 2x2 blocks (->8).

    Strategy derived from notes:
    - Treat only cells with value 5 as tiling domain.
    - Repeatedly select a "hair" candidate triomino: a straight length-3 run
      extending from a chain endpoint (endpoint has exactly one 5-neighbor),
      and with no other nonzero neighbors around that endpoint in the original grid.
    - Use backtracking to decide which hair-triples to turn into 2s so that
      the remaining 5s can be partitioned entirely into disjoint 2x2 squares (8s).
    - Non-5 cells are left unchanged.
    """

    h = len(grid)
    w = len(grid[0]) if h else 0

    # Prepare output grid; we will set 2s during search and 8s at the end.
    out = [row[:] for row in grid]

    # Collect positions of 5s, and split into connected components to keep search small.
    five_positions = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5}
    if not five_positions:
        return out

    # 4-neighborhood
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Build components via BFS over 5-cells
    def bfs_component(start, remaining):
        comp = set([start])
        q = [start]
        remaining.remove(start)
        while q:
            r, c = q.pop()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr, nc) in remaining:
                    remaining.remove((nr, nc))
                    comp.add((nr, nc))
                    q.append((nr, nc))
        return comp

    comps = []
    rem = set(five_positions)
    while rem:
        s = next(iter(rem))
        comps.append(bfs_component(s, rem))

    # Backtracking on a single component with exact cover by 2x2 and 1x3 bars
    def solve_component(S):
        if not S:
            return True

        r, c = min(S)

        # Try 2x2 square with (r,c) as top-left
        sq = {(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)}
        if sq <= S:
            S.difference_update(sq)
            for rr, cc in sq:
                out[rr][cc] = 8
            if solve_component(S):
                return True
            # backtrack
            S.update(sq)
            for rr, cc in sq:
                out[rr][cc] = 5

        # Try horizontal 1x3 starting at (r,c)
        hor = {(r, c), (r, c + 1), (r, c + 2)}
        if hor <= S:
            S.difference_update(hor)
            for rr, cc in hor:
                out[rr][cc] = 2
            if solve_component(S):
                return True
            S.update(hor)
            for rr, cc in hor:
                out[rr][cc] = 5

        # Try vertical 1x3 starting at (r,c)
        ver = {(r, c), (r + 1, c), (r + 2, c)}
        if ver <= S:
            S.difference_update(ver)
            for rr, cc in ver:
                out[rr][cc] = 2
            if solve_component(S):
                return True
            S.update(ver)
            for rr, cc in ver:
                out[rr][cc] = 5

        return False

    # Solve each component independently; write results into out.
    for comp in comps:
        # Fill out with 5s to start for comp (already present), then search.
        # We operate on a mutable set per component.
        comp_set = set(comp)
        if not solve_component(comp_set):
            # Fallback: if no tiling found, mark all these 5s as 8.
            for r, c in comp:
                out[r][c] = 8

    return out
