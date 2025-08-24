def p(g):
 m=len(g[0]);f=sum(g,[]);i=f.index;a,b=divmod(i(2),m);c,d=divmod(i(8),m)
 while b-d:b+=d>b or-1;g[a][b]=4
 while a-c:g[a][d]=4;a+=c>a or-1
 return g
