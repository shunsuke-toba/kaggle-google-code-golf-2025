def p(g):
    """Move each interior point straight (up/down/left/right) to touch the matching-colored border."""
    h, w = len(g), len(g[0])

    # Keep borders as-is, clear interior
    out = [[0] * w for _ in range(h)]
    out[0] = g[0][:]
    out[-1] = g[-1][:]
    for i in range(1, h - 1):
        out[i][0] = g[i][0]
        out[i][-1] = g[i][-1]

    # Edge colors (corners are 0; edges are uniform and all different)
    top = g[0][1]
    bottom = g[-1][-2]
    left = g[1][0]
    right = g[-2][-1]

    # For each interior point, move it to the adjacent cell next to its matching edge
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            v = g[i][j]
            if not v:
                continue
            if v == top:
                out[1][j] = v
            elif v == bottom:
                out[h - 2][j] = v
            elif v == left:
                out[i][1] = v
            elif v == right:
                out[i][w - 2] = v
            # If a color doesn't match any edge (shouldn't happen), ignore it

    return out