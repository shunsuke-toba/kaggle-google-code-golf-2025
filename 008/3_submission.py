def p(g):
 i=f=0;k=4
 while k:
  f+=8in g[i]
  if f>sum(g[i]):g+=g.pop(i),
  else:i+=1
  if 2in g[i]:g=[*map(list,zip(*g[::-1]))];k-=1;i=f=0
 return g
