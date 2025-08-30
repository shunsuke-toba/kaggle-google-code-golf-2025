def p(g):
 g=[[*map(max,a,b[::-1],a[::-1],b)]for a,b in zip(g,g[::-1])]
 for i in 1,3,5:
  for k in range(i+2,17-i,2):g[i][k]=g[~i][k]=g[k][i]=g[k][~i]=g[i][i+2]
 return g