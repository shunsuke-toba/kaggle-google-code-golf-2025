def p(g,r=range,n=0):
 while 0in g[n]:n+=1
 s=n+1;m=len(t:=g[::s]);R=m-2;p=max(([t[i//R+k//3][(i%R+k%3)*s]for k in r(9)]for i in r(R*R)),key=sum)
 for i in r(m*m):
  for k in r(9*(t[i//m][i%m*s]==p[4])):
   for j in r(n*n*(m>(u:=i//m+k//3-1)>-1<(v:=i%m+k%3-1)<m)):g[u*s+j//n][v*s+j%n]=p[k]
 return g