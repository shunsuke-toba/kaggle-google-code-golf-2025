p=lambda g:[[8 if 0<r<len(g)-1 and 0<c<len(row)-1 and g[r-1][c]==g[r+1][c]==row[c-1]==row[c+1]==a>0 else a for c,a in enumerate(row)]for r,row in enumerate(g)]
