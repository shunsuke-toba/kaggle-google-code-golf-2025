def p(g):
 a,b={*str(g)}-{*'[], 08'}
 for _ in[0]*160:g=[[*map(int,str(r)[1::3].replace('0'+b,a+b)[::-1].replace('0'+a,b+a))]for r in zip(*g)]
 return g