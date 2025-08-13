def p(grid):
    def solve(grid, stride, offset, only_same_i):
        M = len(grid[0])
        patterns = []
        zero = True
        pattern_height = 0
        pattern_height_cur = 0
        for r in range(len(grid)):
            if all(cell == 0 for cell in grid[r]):
                zero = True
            elif zero:
                patterns.append(r)
                zero = False
                pattern_height_cur = 1
            else:
                pattern_height_cur += 1
            pattern_height = max(pattern_height, pattern_height_cur)

        # 1番上のパターン（基準パターン）
        reference_pattern = patterns[0]
        
        # 2番目以降のパターンを処理
        for block_idx in range(1, len(patterns)):
            pattern_row = patterns[block_idx]
            pattern_row += offset
            done = False
            for i in reversed(range(M-stride)):
                if done:
                    break
                pat = 0
                for j in range(pattern_height):
                    for k in range(stride):
                        if i+k < M: pat += grid[pattern_row + j][i + k] << (k * pattern_height + j)
                rest = False
                for j in range(pattern_height):
                    for k in range(stride, stride+2):
                        if i+k < M and grid[pattern_row + j][i + k] > 0:
                            rest = True
                if rest:
                    continue
                # 一番上のパターンについて全てのパターンハッシュを計算
                for i2 in range(M-stride):
                    if only_same_i and i2 != i:
                        continue
                    pat2 = 0
                    for j2 in range(pattern_height):
                        for k2 in range(stride):
                            if i2+k2 < M: pat2 += grid[reference_pattern + j2][i2 + k2] << (k2 * pattern_height + j2)
                    if pat == pat2:
                        col1 = i2 + stride
                        col2 = i2 + stride+1
                        check = True
                        for l in range(pattern_height):
                            if grid[reference_pattern + l][col1] != grid[reference_pattern + l][col1+2]:
                                check = False
                                break
                        if not check:
                            continue
                        for d in range(M-i-stride):
                            k = i + stride + d
                            for l in range(pattern_height):
                                grid[pattern_row + l][k] = grid[reference_pattern + l][col1 if d%2 == 0 else col2] // 8
                        done = True
                        break
            if not done:
                return None
        return grid

    grid_copy = [row[:] for row in grid]
    for stride in [3, 2]:
        for only_same_i in [True, False]:
            for offset in [0, -1]:
                grid = [row[:] for row in grid_copy]
                result = solve(grid, stride, offset, only_same_i)
                if result is not None:
                    return result

    return None