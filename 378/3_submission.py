import re;p=lambda g,k=8:k and p(eval(re.sub(r'0(?=(.{%d}.)*.{%d}(, [^0])\2.{%d}0\2.{%d}(.))'%(n:=len(g)*3-2,n-5,n,n-3),r'\3',str([*zip(*g[::-1])]))),k-1)or g
