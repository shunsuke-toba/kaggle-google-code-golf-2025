p=lambda g:(b:=eval(str(g)),[exec('g[r][c]=8')for r in range(1,len(g)-1)for c in range(1,len(g[0])-1)if b[r][c]==b[r][c+1]==b[r][c-1]==b[r+1][c]==b[r-1][c]>0])and g
