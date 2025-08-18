def p(j):
 n=len(j[0]);s=sum(a:=j,[])
 y,j,Y,J=divmod(s.index(2),n)+divmod(s.index(3),n)
 while j-J:a[y][j:=j+(J>j)*2-1]=8
 while(y:=y+(Y>y)*2-1)-Y:a[y][J]=8
 return a
