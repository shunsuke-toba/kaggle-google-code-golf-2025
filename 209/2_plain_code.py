def p(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Step 1: Find rectangle bounded by 4s
    corners = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 4:
                corners.append((r, c))
    
    # Get rectangle boundaries
    min_r = min(r for r, c in corners)
    max_r = max(r for r, c in corners)
    min_c = min(c for r, c in corners)
    max_c = max(c for r, c in corners)
    
    # Step 2: Find patterns outside the rectangle
    # 残った数字部分を含むような最小の長方形を探す
    min_pattern_r = rows
    max_pattern_r = -1
    min_pattern_c = cols
    max_pattern_c = -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and not (min_r <= r <= max_r and min_c <= c <= max_c):
                min_pattern_r = min(min_pattern_r, r)
                max_pattern_r = max(max_pattern_r, r)
                min_pattern_c = min(min_pattern_c, c)
                max_pattern_c = max(max_pattern_c, c)

    max_area = 0
    best_scale = 1
    best_position = None
    scaled_pattern = [None] * 5
    for scale in [2, 3, 4]:
        # Step 3: Scale the pattern
        scaled_pattern[scale] = [[0] * ((max_pattern_c - min_pattern_c + 1)*scale) for _ in range((max_pattern_r - min_pattern_r + 1)*scale)]
        for r in range(len(scaled_pattern[scale])):
            for c in range(len(scaled_pattern[scale][0])):
                scaled_pattern[scale][r][c] = grid[min_pattern_r + r // scale][min_pattern_c + c // scale]
        # 4で囲まれた長方形内で共通部分が最大の場所を探す
        for r in range(min_r, max_r - len(scaled_pattern[scale]) + 2):
            for c in range(min_c, max_c - len(scaled_pattern[scale][0]) + 2):
                match = True
                area = 0
                for sr in range(len(scaled_pattern[scale])):
                    for sc in range(len(scaled_pattern[scale][0])):
                        if grid[r + sr][c + sc] != 0:
                            if grid[r + sr][c + sc] != scaled_pattern[scale][sr][sc]:
                                match = False
                            area += 1
                if match and area > max_area:
                    max_area = area
                    best_scale = scale
                    best_position = (r, c)
    # Step 4: Place the pattern in the rectangle
    r, c = best_position
    for sr in range(len(scaled_pattern[best_scale])):
        for sc in range(len(scaled_pattern[best_scale][0])):
            grid[r + sr][c + sc] = scaled_pattern[best_scale][sr][sc]
    return [[grid[r][c] for c in range(min_c, max_c + 1)] for r in range(min_r, max_r + 1)]