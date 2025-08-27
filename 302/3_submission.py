def p(g):
 for x in range(132):
  if g[y:=x%11][x:=x//11]&g[y+1][x-1]:
   for t in g[y+1-(s:=g[y][x-1::-1].index(5)):y+1]:t[x-s:x]=[s+5]*s
 return g