def p(g,e=enumerate):
 for i,j,h in[(i,j,max(map(sum,g))<8)for i,r in e(g)for j,v in e(r)if v%3]:g[i][j]^=2;g[i+2*h][j+2-2*h]^=2
 return g