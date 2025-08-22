def p(g):
 h=len(g);w=len(g[0]);m=max(sum(g,[]))
 q=[(y,x)for y in range(h)for x in range(w)if g[y][x]<1<(g[y].count(m)*2>w)+(sum(r[x]==m for r in g)*2>h)+1]
 for y,x in q:
  for Y,X in (y,x),(y+1,x),(y-1,x),(y,x+1),(y,x-1):
   if h>Y>=0<=X<w and g[Y][X]<1:g[Y][X]=4;q+=(Y,X),
 return[[c or 3 for c in r]for r in g]
