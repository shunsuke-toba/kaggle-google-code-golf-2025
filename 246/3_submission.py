def p(g):
 b=len(g[0]);i=sum(g,[]).index;d=divmod;y,x=d(i(2),b);Y,X=d(i(3),b)
 while x-X:x+=X>x or-1;g[y][x]=8
 while y-Y:g[y][X]=8;y+=Y>y or-1
 return g
