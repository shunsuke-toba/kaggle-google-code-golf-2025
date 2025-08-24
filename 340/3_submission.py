def p(g):
 for r in g[1:-1]:
  for j,c in enumerate(r[2:-2],2):r[j]=0;r[1]+=c*(c==r[0]);r[-2]+=c*(c==r[-1]);g[1][j]+=c*(c==g[0][j]);g[-2][j]+=c*(c==g[-1][j])
 return g
