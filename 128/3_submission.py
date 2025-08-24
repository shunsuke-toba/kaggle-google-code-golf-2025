p=lambda g:[*zip(*[c[(h:=15-c.count(0)):]+(0,)*h for c in zip(*g)])]
