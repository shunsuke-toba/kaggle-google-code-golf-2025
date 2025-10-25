import re
p=lambda g,k=35:-k*g or p(eval(re.sub('0(?=(, 8){,%d}(.{32}){,%d}[^3]{%d}(.{28}0, 3){%d}.{%d}3)'%(n:=k%3,n,3*n+6,-~n,28-3*n),'8',str([*zip(*g[::-1])]))),k-1)