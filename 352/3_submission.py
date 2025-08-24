def p(g):
 for i,r in enumerate(g):
  for j,v in enumerate(r):r[j]|=v<2 and any(2 in s[(j and j-1):j+2]for s in g[(i and i-1):i+2])
 return g