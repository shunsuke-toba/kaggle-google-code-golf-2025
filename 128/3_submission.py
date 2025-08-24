p=lambda g:[*map(list,zip(*[c[(h:=c[-1]and c.count(c[-1])):]+(0,)*h for c in zip(*g)]))]
