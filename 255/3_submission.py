def p(g,r=range(30)):
 for _ in g*4:
  u=-1
  for d in[i for i in r if{*g[i][5:]}-{0,3,13}]+[30]:
   for e in g[u+2:d-1]*(d-u>6):e[5:]=[13]*25
   u=d
  for i in r:
   if all(b'\n'<bytes(b).strip(b'\0\3')for b in g[:i+2][-3:]):u=g[i].index(13);g[i][:u]=u*[3]
  g=[*map(list,zip(*g[::-1]))]
 return[[x%10for x in b]for b in g]