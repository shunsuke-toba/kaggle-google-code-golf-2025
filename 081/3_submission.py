def p(g):
 for i in range(36):
  if sum(l:=g[y:=i//6][(x:=i%6):x+2]+g[y+1][x:x+2])>23:i=l.index(0);g[y+i//2][x+i%2]=1
 return g
