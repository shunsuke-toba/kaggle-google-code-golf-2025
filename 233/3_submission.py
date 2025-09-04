def p(g):
 R=range;T=R(3);Z=zip;F=filter;L=len;t=[]
 for y in R(L(g)-2):
  for x in R(L(g[0])-2):
   if 0<min(m:=sum(b:=[g[y+i][x:x+3]for i in T],[]))<max(m):
    t+=(-m.count(2),b),
    for i in T:g[y+i][x:x+3]=0,0,0
 g=[*map(list,Z(*F(any,Z(*F(any,g)))))]
 for _,b in sorted(t):
  while not any((q:=(y,x))for y in R(L(g)-2)for x in R(L(g[0])-2)if all(g[y+i][x+j]==2*(b[i][j]!=2)for i in T for j in T)):b=[*Z(*b[::-1])]
  for i in T:y,x=q;g[y+i][x:x+3]=b[i]
 return g