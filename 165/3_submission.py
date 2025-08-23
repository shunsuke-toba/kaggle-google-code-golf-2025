r=range(20)
def p(g):
 k=min(k for y in r[1:]for x in r[1:-1]if(k:=g[y][x])==g[y-1][x]==g[y][x-1]==g[y][x+1]>0)
 for x in r:
  y=c=0
  try:
   while g[~y][x]-k:c|=g[~y][x];y+=1
   for t in g[-y:]*c:t[x]=c
  except:0
 return g
