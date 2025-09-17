def p(g):
 for s in[sum({*sum(g,[])})-8]*44:g=[(a:=0)or[a:=c or a&7and s-a for c in r]for r in zip(*g[::-1])]
 return g