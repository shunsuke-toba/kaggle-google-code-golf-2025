import re
def p(g):
 S=re.sub;g=eval(S('0','2',str(g)))
 for _ in[0]*96:g=[[*map(int,S('2(?=3|$)','3',str(r)[-2::-3]))]for r in zip(*g)]
 return g