def p(g):
 o=eval(str(g));n=len(o)
 for m in range(n*n):
  if(u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   while i<n>g[i][j]>0:i+=1;d=j
   while d<n>u[d]>0:d+=1;w=d-j;r=w>>1;l=j-r-n;a=m//n-r-n
   for y in o[i:]:y[j:d]=[1]*w
   for y,u in zip(o[a:i+r],g[a:]):y[l:d+r]=[c or 3for c in u[l:d+r]]
 return o