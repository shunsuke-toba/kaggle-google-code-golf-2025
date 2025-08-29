import re
def p(g):
 S=re.sub;g=eval(S('0','4',str(g)))
 for _ in[0]*96:g=[[*map(int,S('4(?=0|$)','0',str(r)[-2::-3]))]for r in zip(*g)]
 return g