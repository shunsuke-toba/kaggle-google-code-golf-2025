import re
p=lambda g:[[int(re.search('([1-9])(, 0)+, \\1',str(g))[1])]]