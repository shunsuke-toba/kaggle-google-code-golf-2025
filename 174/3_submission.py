def p(g):
 r=range(10)
 for c in {*sum(g,[])}-{0}:
  u,v=zip(*((i,j)for i in r for j in r if g[i][j]==c));m=[r[min(v):max(v)+1]for r in g[min(u):max(u)+1]]
  if m==[r[::-1]for r in m]:return m
