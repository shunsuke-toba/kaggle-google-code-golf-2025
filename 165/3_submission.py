r=range(20)
def p(g):
 k=min(k for y in r[1:]for x in r[1:-1]if(k:=g[y][x])==g[y-1][x]==g[y][x-1]==g[y][x+1]>0)
 for x in r:
  c=0
  for y in r:
   v=g[~y][x]
   if v==k:
    for t in g[-y:]*c:t[x]=c
    break
   c|=v
 return g
