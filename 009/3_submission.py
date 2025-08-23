def p(g):
 b=g[0][2]
 for _ in 0,1:
  for r in g:
   for c in{*r}-{0,b}:
    try:i=r.index(c)+2;j=r.index(c,i);r[i:j]=[(c+10,b)[x==b]for x in r[i:j]]
    except:0
  g=[*map(list,zip(*g))]
 return[[x%10for x in r]for r in g]
