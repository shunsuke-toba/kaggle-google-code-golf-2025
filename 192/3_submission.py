import re
p=lambda g,k=23:-k*g or p(eval(re.sub(rf'(\d), [^0](?=, \1|{", 0|"*(k<12)}\))',r'\1, \1',str([*zip(*g[::-1])]))),k-1)