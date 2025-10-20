import re
p=lambda g,k=4:k and p(eval(re.sub(r'(1.{6})(.{25})1.{5}1(.{25})\1',r'0,2,0\2 2,2,2\3 0,2,0',str(g))),k-1)or g