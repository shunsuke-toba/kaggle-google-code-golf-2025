def p(g,R=range,n=0):
 while 0 in g[n]:n+=1
 s=n+1;m=len(g)//s+1;p=max(([g[(y+i//3)*s][(x+i%3)*s]for i in R(9)]for y in R(m-2)for x in R(m-2)),key=sum)
 for i in R(m*m):
  for k in R(9*(g[i//m*s][i%m*s]==p[4])):
   for j in R(n*n*(m>(u:=i//m+k//3-1)>-1<(v:=i%m+k%3-1)<m)):g[u*s+j//n][v*s+j%n]=p[k]
 return g