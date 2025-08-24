def p(g,R=range,L=len):
 s=sum(g,[])
 C=sorted({*s},key=s.count);z=C.pop()
 def F(c,h=g):
  for _ in R(4):
   while c not in h[0]:h=h[1:]
   h=[*zip(*h[::-1])]
  return[[x==c for x in r]for r in h]
 for c in C:
  for d in C:
   q,r=F(c),F(d);A=L(r);B=L(r[0])
   for i in R(L(q)*2-A+1):
    for j in R(L(q[0])*2-B+1):
     if c-d and all(q[i+x>>1][j+y>>1]==r[x][y]for x in R(A)for y in R(B)):
      return[[[z,c][x]for x in t]for t in q]
