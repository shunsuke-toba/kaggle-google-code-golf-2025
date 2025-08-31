def p(g,R=range):
 n=len(o:=eval(str(g)))
 for m in R(n*n):
  if(u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   while i<n>g[i][j]>0:i+=1;d=(*u,0).index(0,j);r=d-j>>1;l=max(j-r,0)
   for y in o[i:]:y[j:d]=[1]*r*2
   for k in R(max(m//n-r,0),min(i+r,n)):o[k][l:d+r]=[c or 3for c in g[k][l:d+r]]
 return o