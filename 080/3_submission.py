def p(g):
 R=range;n=0
 while g[n]!=g[n][:1]*len(g[n]):n+=1
 s=n+1;m=-~len(g)//s;A=[g[i*s][::s]for i in R(m)];b=0
 for i in R((m-2)**2):
  y,x=divmod(i,m-2);t=[r[x:x+3]for r in A[y:y+3]];u=sum(map(bool,sum(t,[])))
  if u>b:b=u;P=t
 for i in R(m*m):
  y,x=divmod(i,m)
  if A[y][x]==P[1][1]:
   for k in R(9):
    u,v=y+k//3-1,x+k%3-1
    if 0<=u<m>v>=0:A[u][v]=P[k//3][k%3]
 for y in R(m):
  for x in R(m):
   for j in R(n):g[y*s+j][x*s:x*s+n]=[A[y][x]]*n
 return g
