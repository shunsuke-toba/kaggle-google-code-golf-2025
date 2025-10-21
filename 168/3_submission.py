import re
p=lambda g,k=27:-k*g or p(eval(re.sub(r'0((.{35})+, ([^0]).{28}\3, \3)',r'\3\1',str([*zip(*g[::-1])]))),k-1)