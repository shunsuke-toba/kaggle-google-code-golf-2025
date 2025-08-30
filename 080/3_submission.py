def p(g,R=range,n=0):
 while 0 in g[n]:n+=1
 s=n+1;a=[r[::s]for r in g[::s]];m=len(a);p=max(([a[y+i//3][x+i%3]for i in R(9)]for y in R(m-2)for x in R(m-2)),key=sum)
 for i in R(m*m):
  for k in R(9*(a[y:=i//m][x:=i%m]==p[4])):
   for j in R(n*n*(m>(u:=y+k//3-1)>=0<=(v:=x+k%3-1)<m)):g[u*s+j//n][v*s+j%n]=p[k]
 return g