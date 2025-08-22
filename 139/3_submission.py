def p(g):
 for k in range(49):
  y=k//7;x=k%7
  q=[s[x:x+3]for s in g[y:y+3]];t=[*zip(*q)]
  if min(map(max,q[::2]+t[::2])):
   for w in 0,1,2:g[y+w][x:x+3]=[v or 7 for v in q[w]]
 return g
