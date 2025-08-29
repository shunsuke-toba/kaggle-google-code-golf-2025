def p(g,r=str.replace):
 g=eval(r(str(g),'0','4'))
 for _ in[0]*96:g=[[*map(int,r('0'+str(R)[-2::-3],'04','00')[1:])]for R in zip(*g)]
 return g