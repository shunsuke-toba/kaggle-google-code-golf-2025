def p(g):
 for _ in g*4:
  u=-1
  for d in[d for d in range(30)if{*g[d][5:]}-{0,3,13}]+[30]:
   if d>u+6:
    for b in g[u+2:d-1]:b[5:]=[13]*25
   u=d
  for d in[d for d in range(30)if not any(13 not in b or {*b[:b.index(13)]}-{0,3} for b in g[:d+2][-3:])]:
   g[d][:g[d].index(13)]=[3]*g[d].index(13)
  g=[[*b]for b in zip(*g[::-1])]
 return[[d%10 for d in b]for b in g]