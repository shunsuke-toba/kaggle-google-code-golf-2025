def p(g):
 for _ in g*4:
  u=-1
  for d in[d for d in range(30)if{*g[d][5:]}-{0,3,13}]+[30]:
   for b in g[u+2:d-1]*(d-u>6):b[5:]=[13]*25
   u=d
  for d in range(30):
   if all(bytes(b).strip(b'\0\3')>b'\n'for b in g[:d+2][-3:]):u=g[d].index(13);g[d][:u]=[3]*u
  g=[*map(list,zip(*g[::-1]))]
 return[[d%10 for d in b]for b in g]