import re
p=lambda g,k=20:k and p(eval(re.sub(r'0(?=.{25}0, (\d).{28}\1)',r'\1',str([*zip(*g[::-1])]))),k-1)or g