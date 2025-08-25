def p(g):
 n=x=len(g)-1;y=0;d=1;g[0]=[3]*-~n
 while n>0:
  for _ in[0]*n:y+=d;g[y][x]=3
  for _ in[0]*n:x-=d;g[y][x]=3
  n-=2;d=-d
 return g
