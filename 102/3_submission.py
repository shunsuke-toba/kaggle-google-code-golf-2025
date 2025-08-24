def p(g):
 r=range
 for s in r(2,12):
  for y in r(12-s):
   H=g[y+1:y+s]
   for x in r(12-s):
    if all(g[y][x+i]+g[y+s][x+i]+g[y+i][x]+g[y+i][x+s]>19for i in r(s+1))>sum(sum(m[x+1:x+s])for m in H):
     for m in H:m[x+1:x+s]=[2]*~-s
 return g
