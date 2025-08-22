def p(g):h=g[:1];[h.append(r)for r in g if r!=h[-1]];return g==h and h or p([*map(list,zip(*h))])
