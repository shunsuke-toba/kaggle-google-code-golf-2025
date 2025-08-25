def p(g):
 R=range;n=0
 while len({*g[n]})>1:n+=1
 s=n+1;A=[r[::s]for r in g[::s]];m=len(A);p=min(((t:=sum((A[y+i][x:x+3]for i in R(3)),[])).count(0),t)for y in R(m-2)for x in R(m-2))[1]
 for i in R(m*m):
  if A[y:=i//m][x:=i%m]==p[4]:
   for k in R(9):
    u,v=y+k//3-1,x+k%3-1
    if-1<u<m>v>-1:
     for j in R(n):g[u*s+j][v*s:v*s+n]=[p[k]]*n
 return g
