def p(g,e=enumerate):
 C=[0]*10;x=[99]*10;X=[0]*10;y=[99]*10;Y=[0]*10
 for r,l in e(g):
  for c,v in e(l):
   if v:C[v]+=1;x[v]=min(x[v],r);X[v]=max(X[v],r);y[v]=min(y[v],c);Y[v]=max(Y[v],c)
 b=C.index(max(C))
 return[[c for c in r[y[b]:Y[b]+1]]for r in g[x[b]:X[b]+1]]