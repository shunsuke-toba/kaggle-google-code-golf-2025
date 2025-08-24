def p(g):
 r=range
 for s in r(2,6):
  for y in(R:=r(12-s)):
   H=g[y+1:y+s]
   for x in R:
    if all(g[y][x+i]&g[y+s][x+i]&g[y+i][x]&g[y+i][x+s]>4for i in r(s+1))>any(5 in m[x+1:x+s]for m in H):
     for m in H:m[x+1:x+s]=[2]*~-s
 return g
