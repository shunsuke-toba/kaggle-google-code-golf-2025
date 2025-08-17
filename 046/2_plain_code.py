def p(_grid):
    import random
    def solve(grid):
        zero_col = [i for i in range(len(grid[0])) if all(grid[j][i] == 0 for j in range(3))]
        zero_col.append(len(grid[0]))
        l = 0
        for r in zero_col:
            num = 5
            for _ in range(2):
                for i in range(3):
                    for j in range(l, r):
                        if grid[i][j]%5 != 0:
                            num = grid[i][j]
                        elif grid[i][j] == 5:
                            grid[i][j] = num
            l = r+1
        ptr = 0
        shift = 0
        result = [[0]*(len(grid[0])-len(zero_col)+1) for _ in range(3)]
        for j in range(len(grid[0])):
            if j in zero_col:
                shift = random.randint(0,2)
                continue
            for i in range(3):
                result[i][ptr] = grid[(i+shift)%3][j]
            ptr += 1

        # check path
        y = 1
        for j in range(ptr):
            if result[0][j] != 0 and result[1][j] == 0 and result[2][j] != 0:
                return None
            # 数字の上端・下端のy座標を求める
            y1, y2 = 2, 0
            for i in range(3):
                if result[i][j] != 0:
                    y1 = min(y1, i)
                    y2 = max(y2, i)
            if y1 == y:
                y = y2
            elif y2 == y:
                y = y1
            else:
                return None
        return result
    for _ in range(999):
        grid = [[_grid[i][j] for j in range(len(_grid[0]))] for i in range(3)]
        result = solve(grid)
        if result is not None:
            return result
