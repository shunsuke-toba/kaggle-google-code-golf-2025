def p(g):
 H,W=len(g)-1,len(g[0])
 w=W-1
 for b in range(H*W):
  i,j=b//W,b%W
  if g[i][j]!=0:g[i+(j==w)][j+(j<w)]=g[i][j]
 return g