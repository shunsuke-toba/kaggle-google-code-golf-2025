def p(g,k=6401):
 while k:=k-1:
  n=len(g:=[*map(list,zip(*g[::-1]))]);j=k%~-n;i=k//4%n;a=0
  while g[i][j+1]<(x:=g[i][j-a])<3+a:g[i+a][j:]=g[i-a][j:]=[x]*n;a+=1
 return g