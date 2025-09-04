def p(g):
 for i in range(6400):
  g=[*map(list,zip(*g[::-1]))];n=len(g);i//=4;j=i%~-n;i%=n;a=0
  while g[i][j+1]<(x:=g[i][j-a])<3+a:g[i+a][j:]=g[i-a][j:]=[x]*n;a+=1
 return g