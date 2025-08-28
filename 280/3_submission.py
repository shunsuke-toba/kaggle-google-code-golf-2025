def p(g):
 for i in range(2400):
  n=len(g);j=i%~-n;i%=n;a=0;x=2
  while g[i][j+1]<g[i][j-a]==x:g[i+a][j:]=g[i-a][j:]=[x]*(n-j);a+=1;x=3
  if i%4:g=[*map(list,zip(*g[::-1]))]
 return g