import re
p=lambda g,k=3:-k*g or p(eval(re.sub(r'(0, 0, 0)(.{55})\1(.{55})\1',r'1,1,1\2 1,1,1\3 1,1,1',str(g))),k-1)