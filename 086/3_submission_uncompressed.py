def p(g):
 h=[r[:]for r in g]
 for y,r in enumerate(h):
  for x,b in enumerate(r):
   if b>h[y-1][x]+h[y][x-1]<1:
    a=h[y+1][x+1];n=h[y+3][x]//b+1;s=n+2
    for r in g[y-n:y+s+n]:r[x:x+s]=[b]*s
    for r in g[y:y+s]:r[x-n:x+s+n]=[b]*(n+s+n);r[x]=r[x+s-1]=a
    g[y][x:x+s]=r[x:x+s]=[a]*s
 return g