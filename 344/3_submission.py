f=lambda g:[*zip(*eval(str(g).replace('3, 2','8,0').replace('2, 3','0,8')))]
p=lambda g:f(f(g))