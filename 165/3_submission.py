r=range(20)
def p(g):
 k=min(k for y in r[1:]for x in r[1:-1]if(k:=g[y][x])==g[y-1][x]==g[y][x-1]==g[y][x+1]>0)
 for x in r:
  y=c=0
  while y<20 and (b:=g[~y][x])-k:c|=b;y+=1
  for t in g[-y:]*c*(y<20):t[x]=c
 return g
