def p(g,r=range(30),t=lambda x:[*map(list,zip(*x[::-1]))]):
 for _ in' '*4:
  u=-1
  for d in[i for i in r if{*g[i][5:]}-{0,13}]+[30]:
   for e in g[u+2:d-1]*(d-u>6):e[5:]=[13]*25
   u=d
  g=t(g)
 for _ in' '*4:
  for i in r:
   if all(bytes(b).strip(b'\0\3')>b'\n' for b in g[i-(i>0):i+2]):u=g[i].index(13);g[i][:u]=u*[3]
  g=t(g)
 return[[x%10for x in b]for b in g]