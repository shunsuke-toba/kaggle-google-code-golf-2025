def p(g):
 for k in{*sum(g,[])}:
  y=[i for i,r in enumerate(g)if k in r];x=[i for i,c in enumerate(zip(*g))if k in c];a,b=y[0],y[-1];c,d=x[0],x[-1]
  if g[a][c:d+1]==[k]*-~(d-c)==g[b][c:d+1]and all(r[c]==r[d]==k for r in g[a:b+1]):return[r[c+1:d]for r in g[a+1:b]]
