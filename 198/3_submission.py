def p(g):
 R=range;x=max(sum(g,[]));h=len(g);w=len(g[0])
 H=[i for i in R(h)if g[i].count(x)*2>w];V=[i for i,c in enumerate(zip(*g))if c.count(x)*2>h]
 o=[*map(list,g)]
 q=[(y,x)for y in H for x in R(w)if o[y][x]<1]+[(y,x)for x in V for y in R(h)if o[y][x]<1]
 for y,x in q:o[y][x]=4
 while q:
  y,x=q.pop()
  for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
   if h>Y>=0<=X<w and o[Y][X]<1:o[Y][X]=4;q+=[(Y,X)]
 return [[c or 3 for c in r]for r in o]
