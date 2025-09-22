def p(g,r=range,n=0):
 while 0in g[n]:n+=1
 s=n+1;t=g[::s];m=len(t);p=max(([t[y+k//3][s*(x+k%3)]for k in r(9)]for y in r(m-2)for x in r(m-2)),key=sum)
 for y in r(m):
  for x in r(m):
   for k in r(9*(p[4]==t[y][s*x])):
    u=y+k//3-1;v=x+k%3-1
    for j in r(n*n*(m>u>-1)*(m>v>-1)):g[s*u+j//n][s*v+j%n]=p[k]
 return g