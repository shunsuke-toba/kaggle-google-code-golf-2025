def p(grid):
    g = [row[:] for row in grid]
    h, w = len(g), len(g[0])

    # Repeat 8 times
    for rotation in range(8):
        # For each pair of rows i and j
        for i in range(h):
            for j in range(h):
                # If g[i][0] and g[j][0] are both non-zero and equal
                if g[i][0] != 0 and g[j][0] != 0 and g[i][0] == g[j][0]:
                    # Apply g[j][k] |= g[i][k] for all columns
                    for k in range(w):
                        g[j][k] |= g[i][k]

        # Rotate 90 degrees
        g = [[g[h - 1 - j][i] for j in range(h)] for i in range(w)]
        h, w = w, h

    return g