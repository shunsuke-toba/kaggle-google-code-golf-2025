def p(g):
 k=i=f=0
 while k<4:
  m=max(g[i]);i+=1;f+=m>7
  if f>m:g+=g.pop(i:=i-1),
  if m&3:g=[*zip(*g[::-1])];k+=1;i=f=0
 return g