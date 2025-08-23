def p(g):
 f=lambda z:[*map(z.index,filter(min,z))]
 a,b,c,d=f(g)+f([*zip(*g)])
 for i in range(a+1,b):
  for j in range(c+1,d):
   x=g[I:=i][j];y=g[b][j]==x;y-=g[a][j]==x;z=g[i][d]==x;z-=g[i][c]==x
   while(y|z)&(g[I:=I+y][j:=j+z]<1):g[I][j]=x
 return[q[c:d+1]for q in g[a:b+1]]