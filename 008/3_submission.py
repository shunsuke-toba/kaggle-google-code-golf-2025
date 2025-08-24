def p(g):
 k=i=f=0
 while k<4:
  f+=8in(r:=g[i]);i+=1
  if f>sum(r):g+=g.pop(i:=i-1),
  if 2in r:g=[*zip(*g[::-1])];k+=1;i=f=0
 return g
