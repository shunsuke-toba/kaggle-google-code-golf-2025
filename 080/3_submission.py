def p(g,R=range,n=0):
 while 0in g[n]:n+=1
 s=n+1;m=len(g)//s+1;r=m-2;p=max(([g[(i//r+k//3)*s][(i%r+k%3)*s]for k in R(9)]for i in R(r*r)),key=sum)
 for i in R(m*m):
  for k in R(9*(g[i//m*s][i%m*s]==p[4])):
   u=i//m+k//3-1;v=i%m+k%3-1
   for j in R(n*n*(m>u>-1<v<m)):g[u*s+j//n][v*s+j%n]=p[k]
 return g