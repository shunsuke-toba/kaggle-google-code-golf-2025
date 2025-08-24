def p(g):
 n=len(g);x,y,v=n-1,0,1;g[0]=[3]*n
 for n in range(n-1,0,-2):
  for _ in[0]*n:g[y:=y+v][x]=3
  for _ in[0]*n:g[y][x:=x-v]=3
  v=-v
 return g
