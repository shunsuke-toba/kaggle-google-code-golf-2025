def p(g):
 h=len(g);w=len(g[0]);m=max(sum(g,[]))
 q=[(y,x)for y in range(h)for x in range(w)if g[y][x]<1and(g[y].count(m)*2>w or sum(r[x]==m for r in g)*2>h)]
 for y,x in q:
  if h>y>=0<=x<w and g[y][x]<1:
   g[y][x]=4;q+=(y+1,x),(y-1,x),(y,x+1),(y,x-1)
 return[[c or 3 for c in r]for r in g]
