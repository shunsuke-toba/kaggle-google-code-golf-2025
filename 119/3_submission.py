import re
p=lambda g,k=40:k and p(eval(re.sub('0(?=(.{35})*.{34}[38].{34}[28])','3',str([*zip(*g[::-1])]))),k-1)or g