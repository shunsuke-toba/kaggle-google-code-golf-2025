def p(g):
 for r in g[1:-1]:
  j=2
  for c in r[2:-2]:r[j]=0;r[1]+=c*(c==r[0]);r[-2]+=c*(c==r[-1]);g[1][j]+=c*(c==g[0][j]);g[-2][j]+=c*(c==g[-1][j]);j+=1
 return g