def p(g):
 g=sum(g,[])
 for t in 3,7:
  p=g.index(7//t)
  while t in g:j=g.index(t);g[p+(k:=j-p)//(abs(k)//15 or abs(k))]=-t;g[j]=0
 return[*zip(*[map(abs,g)]*15)]
