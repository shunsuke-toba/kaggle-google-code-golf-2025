def p(g):
 b=g[0][2]
 for _ in 0,1:
  for r in g:
   for c in{*r}-{0,b}:
    if r.count(c)>2:
     q=r.index(c)+2;j=r.index(c,q);r[q:j]=[(c+10,b)[x==b]for x in r[q:j]]
  g=[*map(list,zip(*g))]
 return[[x%10for x in r]for r in g]
