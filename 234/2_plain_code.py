def p(grid):
    count = 0
    number = 0
    dir = 0
    N = len(grid)
    M = len(grid[0])
    d=1,0,-1,0,1
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] != 0 and ((grid[i-1][j] == 0 and grid[i+1][j] == 0) or (grid[i][j-1] == 0 and grid[i][j+1] == 0)):
                count += 1
                number = grid[i][j]
                grid[i][j] = 0
                for dir2 in range(4):
                    ni, nj = i + d[dir2], j + d[dir2+1]
                    if grid[ni][nj] != number and grid[ni][nj] != 0:
                        dir = dir2
    irange = range(N)
    jrange = range(M)
    if dir==3:
        jrange = range(M-1, -1, -1)
    if dir==0:
        irange = range(N-1, -1, -1)
    for i in irange:
        for j in jrange:
            if grid[i][j] == number:
                ni, nj = i + d[dir] * count, j + d[dir+1] * count
                if grid[ni][nj] == 0:
                    grid[ni][nj] = number
                    grid[i][j] = 0
    return grid