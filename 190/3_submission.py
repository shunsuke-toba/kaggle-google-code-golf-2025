def p(g):
 for b in range(3**8):
  i=b%9%8+1;j=b%89%8+1;k=b&3;a=1-2*(0<k<3);c=k>1or-1
  if g[i+1][j]|g[i-1][j]|g[i][j+1]|g[i][j-1]<1<g[i+a][j+c]+1:g[i-a][j-c]=g[i][j]
 return g
