def p(g):
 t=()
 for p in range(len(g)-2):
  for q in range(len(g[0])-2):
   if 0<min(m:=sum(b:=[g[p+i][q:q+3]for i in range(3)],[]))<max(m):
    t+=(-m.count(2),b),
    for i in range(3):g[p+i][q:q+3]=[0]*3
 g=[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
 for _,b in sorted(t):
  while 1>any((y:=p,x:=q)for p in range(len(g)-2)for q in range(len(g[0])-2)if all(g[p+i][q+j]==2-2*(b[i][j]==2)for j in range(3) for i in range(3))):b=[*zip(*b[::-1])]
  for i in range(3):g[y+i][x:x+3]=b[i]
 return g