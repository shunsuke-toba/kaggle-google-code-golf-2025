def p(g):
 g=[[*map(max,a,b[::-1],a[::-1],b)]for a,b in zip(g,g[::-1])]
 for i in 1,3,5:
  k=i+2
  while k<17-i:g[i][k]=g[~i][k]=g[k][i]=g[k][~i]=g[i][i+2];k+=2
 return g