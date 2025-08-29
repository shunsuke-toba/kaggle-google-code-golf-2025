def p(g,R=range,n=0):
 while 0 in g[n]:n+=1
 s=n+1;A=[x[::s]for x in g[::s]];m=len(A);p=max(([A[y+i//3][x+i%3]for i in R(9)]for y in R(m-2)for x in R(m-2)),key=sum)
 for i in R(m*m):
  for k in R(9*(A[y:=i//m][x:=i%m]==p[4])):
   u,v=y+k//3-1,x+k%3-1
   for j in R(n*n*(0<=u<m>v>=0)):g[u*s+j//n][v*s+j%n]=p[k]
 return g