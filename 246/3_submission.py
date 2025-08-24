def p(g):
 b=len(g[0]);c=sum(g,[]);i=c.index;d=divmod;y,x=d(i(2),b);Y,X=d(i(3),b)
 while x-X:g[y][x:=x+(X>x)*2-1]=8
 while(y:=y+(Y>y)*2-1)-Y:g[y][X]=8
 return g
