def p(g):
 f=lambda z:[i for i,s in enumerate(z)if min(s)];a,b=f(g);c,d=f(zip(*g));e,f=g[a][c+1],g[b][c+1];h,k=g[a+1][c],g[a+1][d]
 for i in range(a+1,b):
  for j in range(c+1,d):
   x=g[i][j];y=(x==f)-(x==e);z=(x==k)-(x==h);I,J=i,j
   while(y|z)&(a<I+y<b)&(c<J+z<d):I+=y;J+=z;g[I][J]=x
 return[q[c:d+1]for q in g[a:b+1]]
