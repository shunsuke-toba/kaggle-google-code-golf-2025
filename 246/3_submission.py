def p(a):
 b=len(a[0]);c=sum(a,[])
 y,x,Y,X=divmod(c.index(2),b)+divmod(c.index(3),b)
 while x-X:a[y][x:=x+(X>x)*2-1]=8
 while(y:=y+(Y>y)*2-1)-Y:a[y][X]=8
 return a
