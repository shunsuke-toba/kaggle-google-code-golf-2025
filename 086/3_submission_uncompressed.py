def p(g):
 h=[r[:]for r in g]
 for y,r in enumerate(h):
  for x,b in enumerate(r):
   if b>h[y-1][x]+h[y][x-1]<1:
    a=h[y+1][x+1];n=h[y+3][x]//b+1
    for r in g[y-n:y+n+n+2]:r[x:x+n+2]=[b]*(n+2)
    for r in g[y:y+n+2]:r[x-n:x+n+n+2]=[b]*(n*3+2)
    for r in g[y:y+n+2]:r[x:x+n+2]=[a]*(n+2)
    for r in g[y+1:y+n+1]:r[x+1:x+n+1]=[b]*n
 return g