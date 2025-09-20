def p(g):
 x=[(g[b],~a)for t in range(99)if g[a:=t//10][b:=t%10]];o=x[0][0][-~x[0][1]]
 for b,a in x:b[a+o]=2-b[a+o]
 return g