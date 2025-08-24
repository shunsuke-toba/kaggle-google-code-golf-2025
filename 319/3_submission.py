def p(g,r=range,l=len):
 s=sum(g,[]);*C,z=sorted({*s},key=s.count)
 def F(c,h=g):
  for _ in r(4):
   while c not in h[0]:h=h[1:]
   h=[*zip(*h[::-1])]
  return[[x==c for x in t]for t in h]
 for c in C:
  for d in C:
   q,u=F(c),F(d)
   if(c-d)*any(all(q[i+x>>1][j+y>>1]==u[x][y]for x in r(l(u))for y in r(l(u[0])))for i in r(l(q)*2-l(u)+1)for j in r(l(q[0])*2-l(u[0])+1)):return[[[z,c][x]for x in t]for t in q]
