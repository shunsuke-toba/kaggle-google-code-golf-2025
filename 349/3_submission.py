def p(g,R=range):
 n=len(g);o=[*map(list,g)]
 for i in R(n):
  for j in R(n):
   if 8<g[i][j]>g[i-1][j]*i|g[i][j-1]*j:
    a=0;b=i
    while j+a<n>g[i][j+a]>8:a+=1
    while b<n>g[b][j]>8:b+=1
    r=a//2;L=max(j-r,0)
    for y in o[b:]:y[j:j+a]=[1]*a
    for k in R(max(i-r,0),min(b+r,n)):o[k][L:j+a+r]=[c//9*6+3for c in g[k][L:j+a+r]]
 return o
