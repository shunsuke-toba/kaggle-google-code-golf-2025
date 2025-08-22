p=lambda g:(b:=[r[:]for r in g],[b[r][c]==b[r][c+1]==b[r][c-1]==b[r+1][c]==b[r-1][c]!=0 and g[r].__setitem__(c,8)for r in range(1,len(g)-1)for c in range(1,len(g[0])-1)],g)[2]
