import re
p=lambda g,k=3:-k*g or p(eval(re.sub(r'0(?=(.{35})+, ([^0]).{28}\2, \2)',r'\2',str([*zip(*g[::-1])]))),k-1)