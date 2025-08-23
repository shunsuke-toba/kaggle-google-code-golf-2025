def p(g):
 r=range;n=len(g)
 for s in r(2,n):
  for y in r(n-s):
   H=g[y+1:y+s]
   for x in r(n-s):
    if all(g[y][x+i]*g[y+s][x+i]*g[y+i][x]*g[y+i][x+s]>624 for i in r(s+1))>sum(sum(m[x+1:x+s])for m in H):
     for m in H:m[x+1:x+s]=[2]*~-s
 return g
