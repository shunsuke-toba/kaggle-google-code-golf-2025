def p(g):
 for _ in 0,1:
  for a in g:
   if(s:=[*filter(None,a)])[1:]:break
  a[:]=(s*8)[-a.index(s[0])%len(s):][:len(a)]
  g=[*map(list,zip(*g))]
 return g
