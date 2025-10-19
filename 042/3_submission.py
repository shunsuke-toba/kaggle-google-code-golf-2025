import re
p=lambda g,k=108:k and p(eval(re.sub('0((, 8){,%d}(.{32}){,%d}.{%d}[^3](.{28}0, 3){%d}.{%d}3)'%(n:=k%3,n,3*n+5,-~n,28-3*n),'8\\1',str([*zip(*g[::-1])]))),k-1)or g