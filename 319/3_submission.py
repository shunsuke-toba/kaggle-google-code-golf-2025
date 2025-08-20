def p(g,R=range,L=len):
 p,C=[],sorted({*(s:=sum(g,[]))},key=s.count)
 for c in C[:3]:
  h=[r for r in g]
  for _ in R(4):
   while h[-1].count(c)<1:h.pop()
   h=[*map(list,zip(*h[::-1]))]
  p+=[[[x*(x==c)for x in r]for r in h]]
 for b in R(9):
  q,r=p[b//3],p[b%3]
  n,m,N,M=L(q)*2,L(q[0])*2,L(r),L(r[0])
  s=[[q[i//2][j//2]for j in R(m)]for i in R(n)]
  for i in R(n-N+1):
   for j in R(m-M+1):
    f=q!=r
    for z in R(N*M):
     x,y=z//M,z%M
     if(s[i+x][j+y]>0)!=(r[x][y]>0):f=0
    if f:return [[x+(x<1)*C[3]for x in r]for r in q]