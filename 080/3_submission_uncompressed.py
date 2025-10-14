def p(g,r=range,n=0):
 while 0in g[n]:n+=1
 s=n+1;m=len(g)//s+1;p=max(([g[s*(y+k//3-1)][s*(x+k%3-1)]for k in r(9)]for y in r(1,m-1)for x in r(1,m-1)),key=sum)
 for y in r(m):
  for x in r(m):
   for k in r(9):
    for j in r(n*n*(m>=y+k//3>0)*(m>=x+k%3>0)*(p[4]==g[s*y][s*x])):g[s*(y+k//3-1)+j//n][s*(x+k%3-1)+j%n]=p[k]
 return g