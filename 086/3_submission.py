def p(g):
 n=len(h:=eval(str(g)))
 for y in range(n*n):
  x=y%n;y//=n;b=h[y][x]
  if b>h[y-1][x]+h[y][x-1]<1:
   s=3+h[y+3][x]//b;a=h[y+1][x+1];Y=y+s;X=x+s;S=s-2
   for r in g[y-S:Y+S]:r[x:X]=[b]*s
   for r in g[y:Y]:r[x-S:X+S]=[b]*(S*3+2);r[x]=r[X-1]=a;g[y][x:X]=g[Y-1][x:X]=[a]*s
 return g