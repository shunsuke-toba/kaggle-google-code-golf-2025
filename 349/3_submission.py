def p(g,R=range):
 n=len(g);s=[r[:]for r in g]
 for i in R(n):
  for j in R(n):
   if s[i][j]>8>(i and s[i-1][j])and 8>(j and s[i][j-1]):
    a=0;b=i
    while j+a<n>s[i][j+a]>8:a+=1
    while b<n>s[b][j]>8:b+=1
    r=a//2;L=max(j-r,0)
    for y in g[b:]:y[j:j+a]=[1]*a
    for y in R(max(i-r,0),min(b+r,n)):g[y][L:j+a+r]=[3+6*(c>8)for c in s[y][L:j+a+r]]
 return g
