def p(g):
 o=[r[:]for r in g];n=len(g)
 for m in range(n*n):
  if(u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   while i<n and g[i][j]:i+=1;d=j
   while d<n and u[d]:d+=1;r=d-j>>1;a=m//n-r-n
   for y in o[i:]:y[j:d]=[1]*(d-j)
   for y,u in zip(o[a:i+r],g[a:]):y[j-r-n:d+r]=[c or 3for c in u[j-r-n:d+r]]
 return o
