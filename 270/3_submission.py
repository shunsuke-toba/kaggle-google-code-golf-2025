def p(g):
 g=sum(g,[]);a=g.index
 for t in 3,7:
  while t in g:p=a(8%t);k=a(t)-p;g[p+k//((l:=abs(k))//15 or l)],g[p+k]=-t,0
 return[*zip(*[map(abs,g)]*15)]
