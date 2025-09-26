def p(g):
 g=sum(g,[]);i=225
 while i:
  if (t:=g[i:=i-1])>2:g[i],k=0,i-g.index(8%t);g[i-k+k//(abs(k)%14)]=t
 return*zip(*[iter(g)]*15),