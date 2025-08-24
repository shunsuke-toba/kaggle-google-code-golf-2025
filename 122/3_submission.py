def p(g,e=enumerate):
 h=(g[0]+g[1]).count(3)==1
 for i,j in[(i,j)for i,r in e(g)for j,v in e(r)if v%3]:g[i][j]^=2;g[i+2*h][j+2-2*h]^=2
 return g