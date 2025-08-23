def p(g):
 for k in{*sum(g,[])}:
  y=[i for i,r in enumerate(g)if k in r];a,b=y[0],y[-1];r=g[a];c=r.index(k);d=len(r)+~r[::-1].index(k)
  if{k}=={*g[a][c:d+1],*g[b][c:d+1],*(v for r in g[a:b+1]for v in(r[c],r[d]))}:return[r[c+1:d]for r in g[a+1:b]]
