def p(g):
 r=range;T=r(3);f=filter;l=len;z=zip;t=[]
 for y in r(l(g)-2):
  for x in r(l(g[0])-2):
   b=[g[y+i][x:x+3]for i in T];m=sum(b,[]);s={*m}
   if{2}<s<s|{0}:
    t+=(-m.count(2),b),
    for i in T:g[y+i][x:x+3]=0,0,0
 g=[*map(list,z(*f(any,z(*f(any,g)))))]
 for _,b in sorted(t):
  while not(q:=next(((y,x)for y in r(l(g)-2)for x in r(l(g[0])-2)if all(g[y+i][x+j]==2*(b[i][j]!=2)for i in T for j in T)),0)):b=[*z(*b[::-1])]
  y,x=q
  for i in T:g[y+i][x:x+3]=b[i]
 return g