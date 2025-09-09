def p(g):
 for _ in g:
  g=[*map(list,zip(*g[::-1]))];f=8in g[-1];i=0
  for h in g[::1-2*f]*(g[6][0]==2):
   k=g[0].index(0);k+=abs(g[-f].index(8)-i-k);h[k]=h[k]or 3;i+=1
 return g