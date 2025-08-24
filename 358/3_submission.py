def p(g):
 for _ in 0,1:
  r=0
  while len({*g[r]})<3:r+=1
  a=g[r];*s,=filter(None,a);a[:]=(s*8)[-a.index(s[0])%len(s):][:len(a)]
  g=[*map(list,zip(*g))]
 return g
