def p(g):
 for i in range(64):j=i%8;i//=8;g[i+1][j+1]-=3*all(all(r[j:j+3])for r in g[i:i+3])
 return g