import re
p=lambda g,k=48:k and p(eval(re.sub(r'(([^0]).{5}\2.{28}(.{32})*)0((.{32})*.{28}([^0]).{5}\6)',r'\1(8)\4',str([*zip(*g)]))),k-1)or g