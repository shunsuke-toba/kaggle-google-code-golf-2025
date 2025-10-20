import re
p=lambda g,k=12:k and p(eval(re.sub('5((, 0)*), [^05]','5,5\\1',str([*zip(*g[::-1])]))),k-1)or g