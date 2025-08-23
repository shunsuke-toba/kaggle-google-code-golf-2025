def p(g,e=enumerate):
 for v in{*sum(g,[])}-{0}:
  k=[(r,c)for r,R in e(g)for c,b in e(R)if b==v][::-1];r,c=k[0]
  for R,C in k:g[R][C]=0;g[R][C+(R<r)*(C<c)]=v
 return g
