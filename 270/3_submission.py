def p(g):
 g=sum(g,[]);a=g.index
 for t in 3,7:
  while t in g:p=a(8%t);d=abs(k:=a(t)-p);g[p+k//(d//15or d)],g[p+k]=-t,0
 return*zip(*[map(abs,g)]*15),