def p(g):
 n=min(len(g),len(g[0]));p,c=[r[:n]for r in g[:n]],[r[-n:]for r in g[-n:]]
 if'8'in str(p):p,c=c,p
 g=range(n*n);return[[p[i//n][j//n]*c[i%n][j%n]//8 for j in g]for i in g]
