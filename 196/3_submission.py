def p(g,R=str.replace):
 e=enumerate;g=eval(R(str(g),'0','2'))
 for _ in[0]*96:g=[[*map(int,R('0'+str(r)[-2::-3],'02','00')[1:])]for r in zip(*g)]
 return[[v%2*(v+2*any(2in R[:j+2][-3:]for R in g[:i+2][-3:]))for j,v in e(r)]for i,r in e(g)]