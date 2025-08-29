def p(g,r=str.replace):
 g=eval(r(str(g),'0','2'))
 for _ in[0]*96:g=[[*map(int,r('3'+str(R)[-2::-3],'32','33')[1:])]for R in zip(*g)]
 return g