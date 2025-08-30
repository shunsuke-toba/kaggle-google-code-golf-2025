def p(g):
 n=len(h:=eval(str(g)))
 for Y in range(n*n):
  if (b:=h[y:=Y//n][x:=Y%n])>h[y-1][x]+h[y][x-1]<1:
   S=h[y+3][x]//b+1;s=S+2;X=x+s
   for r in g[y-S:y+s+S]:r[x:X]=[b]*s
   for r in g[y:y+s]:r[x-S:X+S]=[b]*(S*3+2);r[x]=r[X-1]=a=h[y+1][x+1]
   g[y][x:X]=r[x:X]=[a]*s
 return g