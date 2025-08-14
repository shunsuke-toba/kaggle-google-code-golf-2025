def p(g,L=len,T=(-1,0,1)):
 r=[s[:]for s in g]
 for i in range(L(g)):
  for j in range(L(g[0])):
   if g[i][j]==2:
    for a in T:
     for b in T:
      n,m=i+a,j+b
      if-1<n<L(g)and-1<m<L(g[0])and r[n][m]<1:r[n][m]=1
 return r