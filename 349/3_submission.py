def p(g,R=range):
 n=len(o:=eval(str(g)))
 for m in R(n*n):
  if(u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   d=(u+[0]).index(0,j);b=i
   while b<n>g[b][j]>0:b+=1;r=d-j>>1;l=max(j-r,0)
   for y in o[b:]:y[j:d]=[1]*r*2
   for k in R(max(i-r,0),min(b+r,n)):o[k][l:d+r]=[c or 3for c in g[k][l:d+r]]
 return o