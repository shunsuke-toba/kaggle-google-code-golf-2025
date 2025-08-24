R=range(10)
def p(g):
 for c in{*sum(g,[])}-{0}:
  u,v=zip(*((i,j)for i in R for j in R if g[i][j]==c));m=[r[min(v):max(v)+1]for r in g[min(u):max(u)+1]]
  if m==[r[::-1]for r in m]:return m