def p(g):return list(map(list,zip(*[sorted(c,key=0..__eq__)for c in zip(*g)])))
