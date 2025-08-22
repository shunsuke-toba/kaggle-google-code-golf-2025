R=range
def p(g):
 b=min(g[y][x]for y in R(1,20)for x in R(1,19)if g[y][x]==g[y-1][x]==g[y][x-1]==g[y][x+1]!=0)
 for x in R(20):
  j=i=20
  while i and g[i-1][x]^b:i-=1
  while j>i and(c:=g[j-1][x])in(0,b):j-=1
  if 0<i<j:
   for r in g[i:]:r[x]=c
 return g
