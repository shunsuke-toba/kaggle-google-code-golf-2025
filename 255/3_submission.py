def p(g,t=lambda x:[*map(list,zip(*x[::-1]))]):
 r=range(30);k=max(sum(g,[]))
 for _ in[0]*4:
  a=[i for i in r if k in g[i][5:]];u=-1
  for d in a+[30]:
   if d-u>6:
    for e in g[u+2:d-1]:e[5:]=[10]*25
   u=d
  g=t(g)
 for _ in[0]*4:
  for i in r:
   if all(next((v for v in b if(v-3)*v),0)>9for b in g[i-(i>0):i+2]):p=next(j for j in r if g[i][j]);g[i][:p]=p*[3]
  g=t(g)
 return[[(x,3)[x>9]for x in b]for b in g]