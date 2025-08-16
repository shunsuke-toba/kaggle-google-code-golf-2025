def p(a):
 h=len(a);w=len(a[0]);R=range;m=min;M=max
 z=[(i,j)for i in R(h)for j in R(w)if a[i][j]]
 r,c=zip(*z);k=a[r[0]][c[0]];y,x=m(r),m(c);Y,X=M(r),M(c);d=(Y-y)//2
 while 1:
  for j in R(M(x,0),m(X+1,w)):
   if h>y>=0:a[y][j]=k
   if h>Y>=0:a[Y][j]=k
  for i in R(M(y,0),m(Y+1,h)):
   if w>x>=0:a[i][x]=k
   if w>X>=0:a[i][X]=k
  y-=d;Y+=d;x-=d;X+=d
  if y<0>x and Y>=h<=X>=w:break
 return a
