import re
p=lambda g,k=19:-k*g or p(eval(re.sub(r'0(?=.{25}0, (.).{28}\1)',r'\1',str([*zip(*g[::-1])]))),k-1)