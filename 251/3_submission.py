def p(g):
 import re;s=re.sub;g=eval(s('0','1',str(g)))
 for _ in[0]*96:g=[[*map(int,s('1(?=0|$)','0',str(r)[-2::-3]))]for r in zip(*g)]
 return g