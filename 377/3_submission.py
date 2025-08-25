def p(g):h=g[:1];h+=(r for r in g if r!=h[-1]);return g==h and h or p([*zip(*h)])
