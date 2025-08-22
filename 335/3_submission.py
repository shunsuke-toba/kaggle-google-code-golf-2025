def p(g):
 m=len(g[0]);f=sum(g,[]);a,b=divmod(f.index(2),m);c,d=divmod(f.index(8),m)
 while b-d:b+=1-2*(b>d);g[a][b]=4
 while a-c:g[a][d]=4;a+=1-2*(a>c)
 return g