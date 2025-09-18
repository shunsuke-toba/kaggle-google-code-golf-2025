def p(g,k=99):
 f=lambda i,j:i|j|9-i|9-j>C<g[i][j]and(exec('g[i][j]=C')or-~sum(f(i+d,j)+f(i,j+d)for d in(-1,1)))
 while~k:d=k//10,k%10;C=4;C=5-f(*d);f(*d);k-=1
 return g