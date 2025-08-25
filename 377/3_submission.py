def p(g):h=g[:1];h+=filter(lambda r:r!=h[-1],g);return g==h and h or p([*zip(*h)])
