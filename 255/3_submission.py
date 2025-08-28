def p(g,t=lambda x:[*map(list,zip(*x[::-1]))]):
 r=range(30);k=max(sum(g,[]))
 for _ in[0]*4:
  a=[i for i in r if k in g[i][5:]]
  for i in r:
   d=next((j for j in a if j>i),0);u=next((j for j in a[::-1]if j<i),30)
   if(d-i>1<i-u)*d-u>6:g[i][5:]=[10]*25
  g=t(g)
 for _ in[0]*4:
  for i in r:
   if all(next((v for v in b if(v-3)*v),0)>9for b in g[i-(i>0):i+2]):p=next(j for j in r if g[i][j]);g[i][:p]=[3]*p
  g=t(g)
 return[[(x,3)[x>9]for x in b]for b in g]