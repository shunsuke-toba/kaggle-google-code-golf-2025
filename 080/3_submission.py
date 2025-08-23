def p(g):
 R=range;n=0
 while len({*g[n]})>1:n+=1
 s=n+1;A=[r[::s]for r in g[::s]];m=len(A)
 P=min(((str(t:=[r[x:x+3]for r in A[y:y+3]]).count('0'),t)for y in R(m-2)for x in R(m-2)))[1];c=P[1][1]
 for i in R(m*m):
  y,x=divmod(i,m)
  if A[y][x]==c:
   for k in R(9):
    u,v=y+k//3-1,x+k%3-1
    if 0<=u<m>v>=0:
     w=P[k//3][k%3];A[u][v]=w
     for j in R(n):g[u*s+j][v*s:v*s+n]=[w]*n
 return g
