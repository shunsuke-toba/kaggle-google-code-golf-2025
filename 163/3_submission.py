def p(g):
 for i,r in enumerate(g):
  if 4 in r:j=r.index(4);break
 a=i&-4;b=j&-4;i%=4;j%=4
 h=[[0]*11 for _ in g]
 h[3]=h[7]=g[3]
 for r in h:r[3]=r[7]=5
 for k in range(3):h[i*4+k][j*4:j*4+3]=g[a+k][b:b+3]
 return h
