def p(g):
 x=[(g[b],~a)for t in range(100)if g[a:=t//10][b:=t%10]];o=0<sum(b[-~a]-b[a]for b,a in x)
 for b,a in x:b[a+o]=2-b[a+o]
 return g