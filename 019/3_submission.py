def p(g):g=[r+r for _ in(0,1)for r in g];h=len(g);w=len(g[0]);[h>i>-1<j<w and(g[i][j]or g[i].__setitem__(j,8))for k in range(h*w)if g[r:=k//w][c:=k%w]&7 for i in(r-1,r+1)for j in(c-1,c+1)];return g
