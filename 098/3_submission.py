def p(g):
 for a,b,c,d in zip(h:=eval(str(g)),h[1:],h[2:],g[1:-1]):
  for j,x in enumerate(b[1:-1],1):d[j]=x*(a[j]+c[j]+b[j-1]+b[j+1]!=4*x)
 return g
