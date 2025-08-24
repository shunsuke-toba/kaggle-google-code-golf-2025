def p(g):
 m=sum(g,[]);m=min({*m}-{0},key=m.count)
 for _ in 0,1:g=zip(*[r for r in g if m in r])
 return[*g]