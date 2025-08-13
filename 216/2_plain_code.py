def p(g):
    N = 20
    max_value = 0
    r1, c1, r2, c2 = 0, 0, 0, 0
    for r in range(N):
        for c in range(N):
            for x in range(r, N):
                for y in range(c, N):
                    ok = True
                    value = 0
                    for i in range(r, x + 1):
                        for j in range(c, y + 1):
                            if g[i][j] == 0:
                                ok = False
                            if g[i][j] == 1:
                                value += 1
                            elif g[i][j] == 2:
                                value += 999
                    if not ok:
                        break
                    if value > max_value:
                        max_value = value
                        r1, c1, r2, c2 = r, c, x, y
    return [[g[r][c] for c in range(c1, c2 + 1)] for r in range(r1, r2 + 1)]