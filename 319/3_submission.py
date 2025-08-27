def p(g,r=range,l=len):
 s=sum(g,[]);*C,B=sorted({*s},key=s.count)
 def f(c,h=g):
  for _ in r(4):
   while c not in h[0]:h=h[1:]
   h=[*zip(*h[::-1])]
  return h
 for c in C:
  for d in C:
   q=f(c);u=f(d);X,Y=l(u),l(u[0])
   if(c-d)*any(all((q[i+x>>1][j+y>>1]==c)==(u[x][y]==d)for x in r(X)for y in r(Y))for i in r(l(q)*2-X+1)for j in r(l(q[0])*2-Y+1)):return[[[B,c][x==c]for x in t]for t in q]