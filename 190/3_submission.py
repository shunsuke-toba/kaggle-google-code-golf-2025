def p(g,b=1280):
 while b:
  b-=1;i=b%8+1;j=b//8%8+1;a=b>>6&1or-1;c=b>>7&1or-1
  if g[i+a][j+c]>g[i+a][j]+g[i][j+c]:g[i-a][j-c]=g[i][j]
 return g