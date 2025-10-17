import re
p=lambda g,k=96:k and p(eval(re.sub('0(.{25}0, ([1-9]).{28}[1-9])',r'\2\1',str([*zip(*g[::-1])]))),k-1)or g