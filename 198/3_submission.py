def p(g):
 R=range(h:=len(g))
 q=[(y,x)for y in R for x in R if g[y][x]<1<sum(g[y]+[r[x]for r in g])>h*max(sum(g,[]))>>1]
 for y,x in q:
  if 0<=y<h>x>=0==g[y][x]:g[y][x]=4;q+=(y+1,x),(y-1,x),(y,x+1),(y,x-1)
 return[[c or 3 for c in r]for r in g]