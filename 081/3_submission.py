import re
p=lambda g,k=8:k and p(eval(re.sub('0(?=, 8.{19}8)','1',str([*zip(*g[::-1])]))),k-1)or g