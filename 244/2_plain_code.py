def p(grid):
    n = len(grid[0])
    for p in range(n):
        first_row = grid[0]
        if first_row[p] != first_row[p+1]:
            p+=2
            result = []
            for i in range(0,n,p):
                row=[]
                for j in range(0,n,p):
                    row.append(grid[i][j])
                result+=[row]
            # 左右反転
            return [row[::-1] for row in result]