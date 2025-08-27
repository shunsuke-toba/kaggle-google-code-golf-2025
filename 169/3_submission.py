def p(g,k=99):
 f=lambda i,j,c=9:-1<i<10>j>-1<4<g[i][j]!=c and(g[i].__setitem__(j,c)or-~sum(f(i+d,j,c)+f(i,j+d,c)for d in(-1,1)))
 while~k:k-=1;d=divmod(k,10);f(*d,5-f(*d))
 return g