def p(g):
 g=eval(str(g).replace('0','1'))
 for _ in[0]*36:g=[[*map(int,(str(r)[-2::-3]+'0').replace('10','00')[:-1])]for r in zip(*g)]
 return g