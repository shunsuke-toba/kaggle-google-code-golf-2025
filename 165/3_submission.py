R=range
def p(g):
 h,w=len(g),len(g[0]);b=min(g[y][x]for y in R(1,h)for x in R(1,w-1)if g[y][x]==g[y-1][x]==g[y][x-1]==g[y][x+1]!=0)
 for x in R(w):
  j=i=h
  while i and g[i-1][x]^b:i-=1
  while j>i and(c:=g[j-1][x])in(0,b):j-=1
  if 0<i<j:
   for r in g[i:]:r[x]=c
 return g
