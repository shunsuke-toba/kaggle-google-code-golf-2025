def p(g):
 o=eval(str(g));n=len(o)
 for m in range(n*n):
  if(u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   while i<n>g[i][j]>0:i+=1;d=(*u,0).index(0,j);r=d-j>>1;l=j-r-n;a=m//n-r-n
   for y in o[i:]:y[j:d]=[1]*r*2
   for y,u in zip(o[a:i+r],g[a:]):y[l:d+r]=[c or 3for c in u[l:d+r]]
 return o
