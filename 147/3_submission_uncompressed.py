import re
p=lambda g,k=4:k and p(eval(re.sub('3, [^0]','8,8',str([*zip(*g[::-1])]))),k-1)or g