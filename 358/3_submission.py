def p(g):
 for _ in 0,0:a=next(r for r in g if(s:=[*filter(None,r)])[1:]);a[:]=(s*8)[-a.index(s[0])%len(s):];g=[*map(list,zip(*g))]
 return g
