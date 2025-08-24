r=range(20)
def p(g):
 k=min(k for y in r[1:]for x in r[1:-1]if(k:=g[y][x])==g[y-1][x]==g[y][x-1]==g[y][x+1]>0)
 for x in r:
  y=20;c=0
  while y and (b:=g[y-1][x])-k:y-=1;c|=b
  for t in g[y:]*c*y:t[x]=c
 return g
