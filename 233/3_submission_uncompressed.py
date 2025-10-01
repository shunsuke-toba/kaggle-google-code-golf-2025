def p(g):
 t=()
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if 0<min(m:=sum(b:=[g[i+k][j:j+3]for k in range(3)],[]))<max(m):
    t+=(-m.count(2),b),
    for k in range(3):g[i+k][j:j+3]=[0]*3
 g=[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
 for _,b in sorted(t):
  while 1>any((y:=i,x:=j)for i in range(len(g)-2)for j in range(len(g[0])-2)if all(g[i+k][j+l]==2-2*(b[k][l]==2)for l in range(3) for k in range(3))):b=[*zip(*b[::-1])]
  for k in range(3):g[y+k][x:x+3]=b[k]
 return g