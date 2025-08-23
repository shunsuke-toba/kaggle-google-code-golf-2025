def p(g):
 b=g[0][2]
 for _ in 0,1:
  for r in g:
   for c in{*r}-{0,b}:i=r.index(c)+2;j=-r[::-1].index(c)-2;r[i:j]=[(x==b)*b or -c for x in r[i:j]]
  g=[*map(list,zip(*g))]
 return[[*map(abs,r)]for r in g]
