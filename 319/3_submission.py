def p(g,R=range,L=len):
 p=[]
 s=sum(g,[])
 C=sorted({*s},key=s.count)
 for c in C[:-1]:
  h=[*g]
  for _ in R(4):
   while c not in h[-1]:h.pop()
   h=[*zip(*h[::-1])]
  p+=[[[x*(x==c)for x in r]for r in h]]
 B=C[-1]
 for b in R(9):
  q,r=p[b//3],p[b%3]
  if q==r:continue
  n,m=L(q)*2,L(q[0])*2
  N,M=L(r),L(r[0])
  s=[[q[i//2][j//2]for j in R(m)]for i in R(n)]
  for i in R(n-N+1):
   for j in R(m-M+1):
    if all((s[i+x][j+y]>0)==(r[x][y]>0)for x in R(N)for y in R(M)):
     return [[x+(x<1)*B for x in r]for r in q]
