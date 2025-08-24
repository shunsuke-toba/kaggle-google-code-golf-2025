def p(g):g=[r*2for r in g*2];h=len(g);w=len(g[0]);[g[i][j]or g[i].__setitem__(j,8)for k in range(h*w)if g[r:=k//w][c:=k%w]%8for i in(r-1,r+1)for j in(c-1,c+1)if h>i>-1<j<w];return g
