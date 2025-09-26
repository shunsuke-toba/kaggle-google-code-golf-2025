def p(g):
 t=[(y,x,b,g[y+1][x+1],1+(g[y+3][x]>0))for y,r in enumerate(g)for x,b in enumerate(r)if b>g[y-1][x]+r[x-1]<1]
 for y,x,b,a,n in t:
  for r in g[y-n:y+n+n+2]:r[x:x+n+2]=[b]*(n+2)
  for r in g[y:y+n+2]:r[x-n:x+n+n+2]=[b]*(n*3+2)
  for r in g[y:y+n+2]:r[x:x+n+2]=[a]*(n+2)
  for r in g[y+1:y+n+1]:r[x+1:x+n+1]=[b]*n
 return g