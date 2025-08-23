def p(g):
 R=range;D=divmod;n=0
 while len({*g[n]})>1:n+=1
 s=n+1;A=[r[::s]for r in g[::s]];m=len(A);b=9
 for i in R((m-2)**2):
  y,x=D(i,m-2);t=[r[x:x+3]for r in A[y:y+3]];u=str(t).count('0')
  if u<b:b,P,c=u,t,t[1][1]
 for i in R(m*m):
  y,x=D(i,m)
  if A[y][x]==c:
   for k in R(9):
    u,v=y+k//3-1,x+k%3-1
    if 0<=u<m>v>=0:A[u][v]=P[k//3][k%3]
 for y in R(m):
  for x in R(m):
   for j in R(n):g[y*s+j][x*s:x*s+n]=[A[y][x]]*n
 return g
