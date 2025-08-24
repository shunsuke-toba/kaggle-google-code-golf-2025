def p(g,R=range):
 n=len(g);o=[*map(list,g)]
 for m in R(n*n):
  i=m//n;j=m%n;a=0;b=i
  if g[i][j]>g[i-1][j]*i|g[i][j-1]*j:
   while j+a<n>g[i][j+a]>0:a+=1
   while b<n>g[b][j]>0:b+=1
   r=a>>1;l=max(j-r,0)
   for y in o[b:]:y[j:j+a]=[1]*a
   for k in R(max(i-r,0),min(b+r,n)):o[k][l:j+a+r]=[c or 3for c in g[k][l:j+a+r]]
 return o
