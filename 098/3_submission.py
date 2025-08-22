def p(g):
 h=[r[:]for r in g]
 for a,b,c,d in zip(h,h[1:],h[2:],g[1:-1]):
  for j in range(1,len(b)-1):d[j]=b[j]*(a[j]+c[j]+b[j-1]+b[j+1]!=4*b[j])
 return g
