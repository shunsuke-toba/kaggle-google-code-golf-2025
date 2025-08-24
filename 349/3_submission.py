def p(g,R=range):
 n=len(o:=eval(str(g)))
 for m in R(n*n):
  if (u:=g[i:=m//n])[j:=m%n]>g[i-1][j]*i|u[j-1]*j:
   a=(u+[0]).index(0,j)-j;b=i
   while b<n>g[b][j]>0:b+=1
   r=a>>1;l=max(j-r,0)
   for y in o[b:]:y[j:j+a]=[1]*a
   for k in R(max(i-r,0),min(b+r,n)):o[k][l:j+a+r]=[c or 3for c in g[k][l:j+a+r]]
 return o