def p(g):
 *z,=zip(*g)
 if g[12:]:return*zip(*p(z)),
 (y,Y),c=zip(*[(z.index(c),s)for c in z if(s:=sum(c))]);*s,=g[0];s[y::Y-y]=(c*8)[:len(s[y::Y-y])];return[s]*len(g)