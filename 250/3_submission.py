import re;p=lambda g,k=7:-k*g or[*zip(*eval(re.sub('(2.{%d})0((,.{%d})*.{%d})5'%((2+k//4*26,)*3),r'\1 5\2 0',str(p(g,k-1)[::-1]))))]
