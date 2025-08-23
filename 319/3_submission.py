def p(g,R=range,L=len):
 s=sum(g,[])
 C=sorted({*s},key=s.count)
 P=[]
 for c in C[:-1]:
  h=[*g]
  for _ in[0]*4:
   while c not in h[-1]:h.pop()
   h=[*zip(*h[::-1])]
  P+=[[[(x==c)*c for x in r]for r in h]]
 for q in P:
  for r in P:
   if q!=r:
    a,b,c,d=L(q)*2,L(q[0])*2,L(r),L(r[0])
    for i in R(a-c+1):
     for j in R(b-d+1):
      if all((q[i+x>>1][j+y>>1]>0)==(r[x][y]>0)for x in R(c)for y in R(d)):
       return[[x or C[-1] for x in t]for t in q]
