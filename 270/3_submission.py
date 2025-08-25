def p(g):
 g=sum(g,[])
 for t in 3,7:
  while t in g:p=g.index(8%t);j=g.index(t);g[p+(j-p)//((k:=abs(j-p))//15 or k)],g[j]=-t,0
 return[*zip(*[map(abs,g)]*15)]
