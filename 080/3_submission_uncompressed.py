def p(g,r=range,n=0):
 while 0in g[n]:n+=1
 s=n+1;m=len(t:=g[::s]);R=m-2;p=max(([t[i//R+k//3][s*(i%R+k%3)]for k in r(9)]for i in r(R*R)),key=sum)
 for i in r(m*m):
  for k in r(9*(p[4]==t[i//m][s*(i%m)])):
   for j in r(n*n*(0<=(u:=i//m+k//3-1)<m)*(0<=(v:=i%m+k%3-1)<m)):g[s*u+j//n][s*v+j%n]=p[k]
 return g