def p(g,R=range):
 for _ in R(96):
  if sum(g[-1])<1:g=g[:-1]
  g=[*map(list,zip(*g[::-1]))]
 return [[(g[i][j]>0)*g[0][0]for j in R(1,len(g[0])-1)]for i in R(1,len(g)-1)]