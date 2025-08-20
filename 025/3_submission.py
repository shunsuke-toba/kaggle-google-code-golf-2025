def p(g,E=enumerate):
 w=len(g[0]);t=[*zip(*g)];o=[[0]*w for _ in g]
 for c in{*sum(g,[])}-{0}:
  for x,col in E(t):
   if col.count(c)==len(g):
    for y,r in E(g):
     o[y][x]=c
     if c in r[:x]:o[y][x-1]=c
     if c in r[x+1:]:o[y][x+1]=c
  for y,r in E(g):
   if r.count(c)==w:
    o[y]=[c]*w
    for x,col in E(t):
     if c in col[:y]:o[y-1][x]=c
     if c in col[y+1:]:o[y+1][x]=c
 return o
