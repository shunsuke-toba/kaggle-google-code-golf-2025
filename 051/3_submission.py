import re
p=lambda g,k=64:k and p(eval(re.sub(r'(0, ([^0]), (?!\2)[^0][^)]+)0',r'\1\2',str([*zip(*g[::-1])]))),k-1)or g