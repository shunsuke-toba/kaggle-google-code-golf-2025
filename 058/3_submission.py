def p(g):
 n=x=len(g)-1;d=1;g[y:=0]=[3]*-~n
 while n>0:
  for i in[d]*n+[0]*n:y+=i;x+=i-d;g[y][x]=3
  n-=2;d=-d
 return g