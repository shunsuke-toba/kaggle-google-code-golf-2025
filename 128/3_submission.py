def p(g):
 h=len(g);a=[[0]*len(g[0])for _ in g];f={}
 for y in range(h):
  for x,c in enumerate(g[y]):
   if c:a[y+f.setdefault(c,y)-h][x]=c
 return a
