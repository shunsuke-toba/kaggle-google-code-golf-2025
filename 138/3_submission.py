def p(g):
 f=lambda z:[i for i,s in enumerate(z)if min(s)];a,b=f(g);c,d=f(zip(*g))
 for i in range(a+1,b):
  for j in range(c+1,d):
   x=g[i][j];y=(x==g[b][c+1])-(x==g[a][c+1]);z=(x==g[a+1][d])-(x==g[a+1][c]);I,J=i,j
   while(y|z)&(a<I+y<b)&(c<J+z<d):I+=y;J+=z;g[I][J]=x
 return[q[c:d+1]for q in g[a:b+1]]
