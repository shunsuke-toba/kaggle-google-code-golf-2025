def p(g):
 *z,=zip(*g)
 if g[12:]:return*zip(*p(z)),
 (y,Y),c=zip(*((i,v)for i,v in enumerate(map(sum,z))if v));*s,=g[0];s[y::Y-y]=(c*8)[:len(s[y::Y-y])];return[s]*len(g)