def p(g):
 f=lambda z:[i for i,r in enumerate(z)if min(r)];a,b,c,d=f(g)+f(zip(*g))
 for i in range(a+1,b):
  for j in range(c+1,d):
   x=g[I:=i][j];y=(x==g[b][j])-(x==g[a][j]);z=(x==g[i][d])-(x==g[i][c])
   while(y|z)&(g[I:=I+y][j:=j+z]<1):g[I][j]=x
 return[q[c:d+1]for q in g[a:b+1]]