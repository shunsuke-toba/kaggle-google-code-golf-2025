def p(g):
 R=range;n=0
 while len({*g[n]})>1:n+=1
 s=n+1;A=[r[::s]for r in g[::s]];m=len(A)
 P=min(((t:=A[y][x:x+3]+A[y+1][x:x+3]+A[y+2][x:x+3]).count(0),t)for y in R(m-2)for x in R(m-2))[1]
 for i in R(m*m):
  y,x=i//m,i%m
  if A[y][x]==P[4]:
   for k in R(9):
    u,v=y+k//3-1,x+k%3-1
    if 0<=u<m>v>=0:
     for j in R(n):g[u*s+j][v*s:v*s+n]=[P[k]]*n
 return g
