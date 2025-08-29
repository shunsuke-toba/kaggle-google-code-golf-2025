def p(g,t=lambda x:[*map(list,zip(*x[::-1]))]):
 r=range(30);k=max(sum(g,[]))
 for _ in' '*4:
  u=-1
  for d in[i for i in r if k in g[i][5:]]+[30]:
   if d-u>6:
    for e in g[u+2:d-1]:e[5:]=[10]*25
   u=d
  g=t(g)
 for _ in' '*4:
  for i in r:
   if all(next((v for v in b if(v-3)*v),0)>9for b in g[i-(i>0):i+2]):u=g[i].index(10);g[i][:u]=u*[3]
  g=t(g)
 return[[x-7*(x>9)for x in b]for b in g]