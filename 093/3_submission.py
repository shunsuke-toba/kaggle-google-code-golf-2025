def p(g):
 r=[[0 if c and c-5 else c for c in r]for r in g];F=lambda a:sum(c and c-5 and 1 for c in a)
 for j,x in enumerate(zip(*g)):
  if 5 in x:
   u=x.index(5);d=len(g)+~x[::-1].index(5);a=F(x[:u])
   while a:r[u-a][j]=5;a-=1
   a=F(x[d+1:])
   while a:r[d+a][j]=5;a-=1
 for i,x in enumerate(g):
  if 5 in x:
   L=x.index(5);R=len(x)+~x[::-1].index(5);a=F(x[:L])
   while a:r[i][L-a]=5;a-=1
   a=F(x[R+1:])
   while a:r[i][R+a]=5;a-=1
 return r
