def p(g):
 h=[r[:]for r in g]
 for y,r in enumerate(h):
  for x,b in enumerate(r):
   if b>h[y-1][x]+h[y][x-1]<1:
    a=h[y+1][x+1];s=h[y+3][x]//b+3;n=s-2;m=x+s
    for r in g[y-n:y+s+n]:r[x:m]=[b]*s
    for r in g[y:y+s]:r[x-n:m+n]=[b]*(n*3+2);r[x]=r[m-1]=a
    g[y][x:m]=r[x:m]=[a]*s
 return g
