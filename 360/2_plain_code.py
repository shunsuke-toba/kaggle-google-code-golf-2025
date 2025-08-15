def p(grid):
    height = len(grid)
    result = []
    
    # 各行について左右の対応する位置のビット論理和を計算
    for i in range(height):
        row = []
        for j in range(4):  # 左半分の4列
            # g[i][j] | g[i][8-j] (j=0→8-0=8, j=1→8-1=7, j=2→8-2=6, j=3→8-3=5)
            left_value = grid[i][j]
            right_value = grid[i][8-j]
            combined = left_value | right_value
            row.append(combined)
        result.append(row)
    
    return result