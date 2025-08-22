def p(g,A=enumerate):
 Y=X=0
 for y,r in A(g):
  for x,v in A(r):Y+=y*v;X+=x*v
 for k in-1,0,1:g[Y//2+k][X//2]=g[Y//2][X//2+k]=3
 return g
