r=range(20)
def p(g):
 b=min(k for y in r[1:]for x in r[1:-1]if(k:=g[y][x])==g[y-1][x]==g[y][x-1]==g[y][x+1]>0)
 for x in r:
  j=i=20
  while i and g[i-1][x]^b:i-=1
  while j>i and(c:=g[j-1][x])in(0,b):j-=1
  for R in g[i:]*(0<i<j):R[x]=c
 return g
