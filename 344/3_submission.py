def p(g):
 for _ in 0,1:g=[*map(list,zip(*[eval(str(r).replace('3, 2','8, 0').replace('2, 3','0, 8'))for r in g]))]
 return g
