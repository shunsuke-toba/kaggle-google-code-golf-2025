def p(grid):
    g = [row[:] for row in grid]
    h, w = len(g), len(g[0])

    # Repeat 8 times
    for iteration in range(8):
        # For each row i (0 to 20, when i=0, i-1=-1 which is fine)
        for i in range(21):
            # For each pair of columns j and k
            for j in range(21):
                for k in range(21):
                    # If g[i-1][j] and g[i-1][k] are both non-zero and equal
                    if g[i-1][j] != 0 and g[i-1][k] != 0 and g[i-1][j] == g[i-1][k]:
                        # Apply g[i][j] |= g[i][k]
                        g[i][j] |= g[i][k]

        # Transpose the grid
        g = [[g[j][i] for j in range(h)] for i in range(w)]
        h, w = w, h

    return g