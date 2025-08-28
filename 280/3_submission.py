def p(g):
 for i in range(2400):
  n=len(g);j=i%~-n;i%=n;a=0
  while g[i][j+1]-a<g[i][j]<g[i][j-a]+(a<1)<4:g[i+a][j:]=g[i-a][j:]=[2+(a>0)]*(n-j);a+=1
  if i%4:g=[*map(list,zip(*g[::-1]))]
 return g