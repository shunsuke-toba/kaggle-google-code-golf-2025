def p(g):h=g[:1];h+=(r for r in g if r!=h[-1]);return h*(g==h)or p([*zip(*h)])
