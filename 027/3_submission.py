def p(g):
 r=range(10);x=[(g[b],~a)for a in r for b in r if g[a][b]];o=sum(b[-~a]-b[a]for b,a in x)>0
 for b,a in x:b[a+o]=2-b[a+o]
 return g