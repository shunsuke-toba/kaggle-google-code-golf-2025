def p(g):
 *z,=zip(*g)
 if g[12:]:return*zip(*p(z)),
 *c,=filter(sum,z);y,Y=map(z.index,c);*s,=g[0];s[y::Y-y]=map(sum,(c*8)[:len(s[y::Y-y])]);return[s]*len(g)