def p(g):
 h=len(g);m=max(sum(g,[]))
 q=[(y,x)for y in range(h)for x in range(h)if g[y][x]<1and max(g[y].count(m),sum(r[x]==m for r in g))*2>h]
 for y,x in q:
  if 0<=y<h>x>=0==g[y][x]:g[y][x]=4;q+=(y+1,x),(y-1,x),(y,x+1),(y,x-1)
 return[[c or 3 for c in r]for r in g]
