def p(g,R=range):
 n=len(g);s=[r[:]for r in g]
 for i in R(n):
  for j in R(n):
   if 8<s[i][j]and(i<1 or s[i-1][j]-9)and(j<1 or s[i][j-1]-9):
    a=c=0
    while j+a<n>s[i][j+a]>8:a+=1
    while i+c<n>s[i+c][j]>8:c+=1
    r=a//2;L=max(j-r,0);E=min(j+a+r,n)
    for y in g[i+c:]:y[j:j+a]=[1]*a
    for y in R(max(i-r,0),min(i+c+r,n)):g[y][L:E]=[9-6*(s[y][x]<9)for x in R(L,E)]
 return g
