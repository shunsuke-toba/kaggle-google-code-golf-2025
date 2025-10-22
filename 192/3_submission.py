import re
p=lambda g,k=23:-k*g or p(eval(re.sub(r'(\d), [^0](?=, \1|, 0|\))',r'\1, \1',str([*zip(*g[::-1])]))),k-1)