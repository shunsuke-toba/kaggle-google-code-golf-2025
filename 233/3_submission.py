def p(g):
 R=range;T=R(3);f=filter;t=[]
 for y in R(len(g)-2):
  for x in R(len(g[0])-2):
   b=[g[y+i][x:x+3]for i in T];s={*sum(b,[])}
   if{2}<s<s|{0}:
    t+=(-str(b).count('2'),b),
    for i in T:g[y+i][x:x+3]=0,0,0
 g=[*map(list,zip(*f(any,zip(*f(any,g)))))]
 for _,b in sorted(t):
  for _ in R(4):
   try:y,x=next((y,x)for y in R(len(g)-2)for x in R(len(g[0])-2)if all((b[i][j]==2)==(g[y+i][x+j]<1)for i in T for j in T));break
   except:b=[*zip(*b[::-1])]
  for i in T:g[y+i][x:x+3]=b[i]
 return g
