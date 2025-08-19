def p(g):
 i,f,k=0,0,0
 while k<4:
  f+=(r:=g[i]).count(8)
  if sum(r)<f:g=g[:i]+g[i+1:]+[r]
  else:i+=1
  if g[i].count(2):g=[*map(list,zip(*g[::-1]))];k+=1;i=f=0
 return g
