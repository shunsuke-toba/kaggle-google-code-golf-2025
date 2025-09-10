def p(g):
 if g[12:]:return*zip(*p([*zip(*g)])),
 (y,Y),c=zip(*sorted((r.index(v),v)for r in g for v in r if v))
 s=list(g[0]);s[y::Y-y]=(c*8)[:len(s[y::Y-y])];return[s]*len(g)