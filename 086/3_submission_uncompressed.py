def p(g):
 n=len(h:=eval(str(g)))
 for Z in range(n*n):
  if(b:=h[y:=Z//n][x:=Z%n])>h[y-1][x]+h[y][x-1]<1:
   T=h[y+3][x]//b+1;X=x+T+2
   for r in g[y-T:y+T+2+T]:r[x:X]=[b]*(T+2)
   for r in g[y:y+T+2]:r[x-T:X+T]=[b]*(T*3+2);r[x]=r[X-1]=a=h[y+1][x+1]
   g[y][x:X]=r[x:X]=[a]*(T+2)
 return g
