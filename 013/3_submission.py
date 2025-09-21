def p(g):
 *z,=zip(*g)
 if g[12:]:return*zip(*p(z)),
 *c,=filter(sum,z);y,Y=map(z.index,c);c=(*map(sum,c),);*s,=g[0];s[y::Y-y]=(c*8)[:len(s[y::Y-y])];return[s]*len(g)