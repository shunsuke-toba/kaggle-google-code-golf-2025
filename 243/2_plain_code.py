def p(grid):
    n=len(grid)
    m=n*n
    for b in range(m*96):
        r,c=b%(m)//n,b%(m)%n
        if c>0 and grid[r][c-1]==1 and grid[r][c]==0:
            grid[r][c]=1
        if b%(m)==0:
            grid = [list(row) for row in zip(*grid[::-1])]
    return grid