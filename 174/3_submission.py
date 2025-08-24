def p(g):
 for c in{*(f:=sum(g,[]))}-{0}:
  u,v=zip(*[divmod(i,10)for i in range(100)if f[i]==c]);m=[r[min(v):max(v)+1]for r in g[min(u):max(u)+1]]
  if m==[r[::-1]for r in m]:return m
