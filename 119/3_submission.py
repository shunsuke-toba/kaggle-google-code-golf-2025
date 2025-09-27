def p(g):
 for _ in g:
  g=[*map(list,zip(*g[::-1]))];p=b=0
  for h in(g[6][0]==2)*g[::8in g[0]or-1]:h[p:=p or h.index(8)]|=3>>h[p];b|=h[p-1];p+=b-1
 return g