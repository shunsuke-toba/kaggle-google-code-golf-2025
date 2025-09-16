def p(g,k=99):
 f=lambda i,j,c=4:i|j|9-i|9-j>c<g[i][j]and(exec('g[i][j]=c')or-~sum(f(i+d,j,c)+f(i,j+d,c)for d in(-1,1)))
 while~k:d=k//10,k%10;f(*d,5-f(*d));k-=1
 return g