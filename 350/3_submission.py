def p(g):
 L=len;R=range;H=L(g);W=L(g[0])
 for k in R(H+W):
  t=k>=H;i=k-H*t
  s=[j for j in R((W,H)[t])if g[i-i*t+j*t][j-j*t+i*t]==1]
  for j in R(s[0],s[-1]+1)if s else[]:
   x,y=i-i*t+j*t,j-j*t+i*t
   if g[x][y]-1:g[x][y]=8
 return g