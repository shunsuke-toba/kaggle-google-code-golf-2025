def p(g):
 for b in range(9**5):
  i,j=b%9%8+1,b%89%8+1;a,c=1-2*(0<(k:=b%4)<3),1-2*(k<2)
  if g[i+1][j]+g[i-1][j]+g[i][j+1]+g[i][j-1]<1<g[i+a][j+c]+1:g[i-a][j-c]=g[i][j]
 return g