def p(g):
 for b in range(1280):
  i=b%8+1;j=b//8%8+1;a=b>>6&1 or-1;c=b>>7&1 or-1
  if g[i+a][j+c]>g[i+1][j]+g[i-1][j]+g[i][j+1]+g[i][j-1]:g[i-a][j-c]=g[i][j]
 return g