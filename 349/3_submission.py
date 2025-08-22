def p(g,R=range):
 n=len(g);s=[r[:]for r in g]
 for i in R(n):
  for j in R(n):
   if 8<s[i][j]and(i<1 or s[i-1][j]-9)*(j<1 or s[i][j-1]-9):
    a=c=0
    while j+a<n>s[i][j+a]>8:a+=1
    while i+c<n>s[i+c][j]>8:c+=1
    r=a//2;t=i-r;b=i+c+r;l=j-r;e=j+a+r;z=[1]*a;T=max(t,0);B=min(b,n);L=max(l,0);E=min(e,n)
    for y in R(i+c,n):g[y][j:j+a]=z
    for y in R(T,B):g[y][L:E]=[(9,3)[s[y][x]<9]for x in R(L,E)]
 return g
