def p(g,R=range):
 n=len(g);o=[*map(list,g)]
 for i in R(n):
  for j in R(n):
   if g[i][j]>8>((i and g[i-1][j])|(j and g[i][j-1])):
    a=0;b=i
    while j+a<n>g[i][j+a]>8:a+=1
    while b<n>g[b][j]>8:b+=1
    r=a//2;L=max(j-r,0)
    for y in o[b:]:y[j:j+a]=[1]*a
    for y in R(max(i-r,0),min(b+r,n)):o[y][L:j+a+r]=[3+6*(c>8)for c in g[y][L:j+a+r]]
 return o
