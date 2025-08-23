def p(g,R=range,L=len):
 s=sum(g,[])
 C=sorted({*s},key=s.count)
 P=[]
 for c in C[:-1]:
  h=g
  for _ in R(4):
   while c not in h[-1]:h=h[:-1]
   h=[*zip(*h[::-1])]
  P+=[[[(x==c)*c for x in r]for r in h]]
 for q in P:
  for r in P:
   for i in R(L(q)*2-L(r)+1):
    for j in R(L(q[0])*2-L(r[0])+1):
     if q!=r and all((q[i+x>>1][j+y>>1]>0)==(r[x][y]>0)for x in R(L(r))for y in R(L(r[0]))):
      return[[x or C[-1] for x in t]for t in q]
