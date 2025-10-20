import re
p=lambda g,k=36:k and p(eval(re.sub('0((.{%d})*.{%d}([^0]), \\3.{%d}0, \\3.{%d}([^0]))'%((n:=len(g)*3)-1,n-5,n-2,n-5),r'\4\1',str([*zip(*g[::-1])]))),k-1)or g