def p(g):
 R,C=len(g),len(g[0]);L=-1
 for r in range(R):
  if g[r][0]==5:L=r
 for b in range(R*C):
  r,b=b//C,b%C
  if g[r][b]%5==0:continue
  d=-1if(g[r][b]-1)!=(r<L)else 1;i=r
  while 0<=i<R and i!=L:g[i][b]=g[r][b];i+=d
 return g