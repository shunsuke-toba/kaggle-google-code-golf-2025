def p(g):
 for x in range(2800):
  n=len(g);i=x%n;j=x%~-n;a=0;k=n-j
  if 3>g[i][j]>g[i][j+1]:
   while g[i][j-a-1]:a+=1;g[i+a][j:]=g[i-a][j:]=[3]*k
   g[i][j:]=[2]*k
  if x%7:g=[*map(list,zip(*g[::-1]))]
 return g