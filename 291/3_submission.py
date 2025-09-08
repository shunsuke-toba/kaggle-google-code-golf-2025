import re
p=lambda g:[[int(re.split(r'([^0])(, 0)+, \1',str(g))[1])]]