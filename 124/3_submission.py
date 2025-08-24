def p(g):
 for k in 1,2,3:
  for d in 0,1,2:
   if g[k:]==[d*[0]+r[:10-d]for r in g[:-k]]:
    while len(g)<10:g+=d*[0]+g[-k][:10-d],
    return g
