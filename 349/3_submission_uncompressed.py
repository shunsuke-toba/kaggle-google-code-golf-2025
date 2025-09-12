def p(g):
 n=len(o:=eval(str(g)))
 for m in range(n*n):
  if(u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   while i<n>g[i][j]>0:i+=1;d=(*u,0).index(0,j);r=d-j>>1;l=j-r-n;a=m//n-r-n;k=d+r
   for y in o[i:]:y[j:d]=[1]*r*2
   for y,x in zip(o[a:i+r],g[a:]):y[l:k]=[c or 3for c in x[l:k]]
 return o