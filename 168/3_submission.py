import re
p=lambda g,k=28:k and p(eval(re.sub(r'0((.{34}[^0])*.{37}([^0]).{28}\3, \3)',r'\3\1',str([*zip(*g[::-1])]))),k-1)or g