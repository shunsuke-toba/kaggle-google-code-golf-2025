def p(g):
 for i in range(64):
  j=i%8;i//=8
  if all(all(r[j:j+3])for r in g[i:i+3]):g[i+1][j+1]=2
 return g
