def p(g):
 n=len(h:=eval(str(g)))
 for y in range(n):
  for x in range(n):
   if(b:=h[y][x])>h[y-1][x]+h[y][x-1]<1:
    a=h[y+1][x+1];s=h[y+3][x]//b+3;S=s-2;X=x+s
    for r in g[y-S:y+s+S]:r[x:X]=[b]*s
    for r in g[y:y+s]:r[x-S:X+S]=[b]*(S*3+2);r[x]=r[X-1]=a
    g[y][x:X]=r[x:X]=[a]*s
 return g
