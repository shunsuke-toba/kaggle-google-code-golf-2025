def p(grid):
    height = len(grid)
    width = len(grid[0])
    
    result = [[8 for _ in range(width)] for _ in range(height)]
    
    # 新しい解法: a=(h-1-i)mod(2w-2)とする
    for i in range(height):
        if width == 1:
            col = 0
        else:
            a = (height - 1 - i) % (2 * width - 2)
            if a < width:
                col = a
            else:
                col = 2 * width - 2 - a
        result[i][col] = 1
    
    return result