def p(g):
 for _ in g:
  g=[*map(list,zip(*g[::-1]))];p=b=0
  for h in(g[6][0]==2)*g[::-(8in g[-1])|1]:p=p or h.index(8);h[p]=h[p]or 3;b|=h[p-1];p+=b-1
 return g