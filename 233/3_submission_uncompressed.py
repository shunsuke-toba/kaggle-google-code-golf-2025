def p(g):
 t=()
 for y in range(len(g)-2):
  for x in range(len(g[0])-2):
   if 0<min(m:=sum(b:=[g[y+i][x:x+3]for i in range(3)],[]))<max(m):
    t+=(-m.count(2),b),
    for i in range(3):g[y+i][x:x+3]=0,0,0
 g=[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
 for _,b in sorted(t):
  while any((y:=Y,x:=X)for Y in range(len(g)-2)for X in range(len(g[0])-2)if all(g[Y+i][X+j]==2*(b[i][j]!=2)for i in range(3) for j in range(3)))<1:b=[*zip(*b[::-1])]
  for i in range(3):g[y+i][x:x+3]=b[i]
 return g
