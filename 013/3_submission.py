def p(g):
 *z,=zip(*g)
 if g[12:]:return*zip(*p(z)),
 *b,=map(sum,z);y,Y=map(b.index,filter(int,b));b[y:]=b[y:2*Y-y]*8;return[b[:len(z)]]*len(g)