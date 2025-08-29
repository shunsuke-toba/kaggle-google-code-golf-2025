def p(g):
 import re;s=re.sub;e=enumerate;g=eval(s('0','2',str(g)))
 for _ in[0]*96:g=[[*map(int,s('2(?=0|$)','0',str(r)[-2::-3]))]for r in zip(*g)]
 return[[v%2*(v+2*any(2in R[:j+2][-3:]for R in g[:i+2][-3:]))for j,v in e(r)]for i,r in e(g)]