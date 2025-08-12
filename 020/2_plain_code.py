def p(grid):
    H, W = len(grid), len(grid[0])

    def inb(r, c):
        return 0 <= r < H and 0 <= c < W

    max_value = 0
    center = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 0:
                continue

            # Center detection per notes
            diags = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            udlr2 = [(-2, 0), (2, 0), (0, -2), (0, 2)]
            count = 0
            value = 0
            for dr, dc in diags:
                if inb(r + dr, c + dc) and grid[r + dr][c + dc] != 0:
                    count += 1
            if count == 4:
                value += 1
            count = 0
            for dr, dc in udlr2:
                if inb(r + dr, c + dc) and grid[r + dr][c + dc] != 0:
                    count += 1
            if count == 4:
                value += 2
            if value > max_value:
                max_value = value
                center = (r, c)

    r = center[0]
    c = center[1]
    # Copy by rotating every source around (r,c)
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v == 0:
                continue
            dr, dc = i - r, j - c
            for rr, cc in ((dr, dc), (-dc, dr), (-dr, -dc), (dc, -dr)):
                tr, tc = r + rr, c + cc
                if inb(tr, tc) and grid[tr][tc] == 0:
                    grid[tr][tc] = v
    return grid
