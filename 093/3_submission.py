def p(g):
 f=lambda r:list(map(list,zip(*r)))
 if T:=all(any(r)for r in g):g=f(g)
 for z in range(9**5):
  x,y=z//14%12+1,z%14
  if g[x][y]>0:g[x][y]=5
  else:g[x][y]=g[i:=(x+1-2*(x<7))][y];g[i][y]=0
 if T:g=f(g)
 return g