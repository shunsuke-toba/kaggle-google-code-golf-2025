def p(g,r=range):
 for c in r(7):
  for E in r(7):
   q=[s[E:E+3]for s in g[c:c+3]];t=[*zip(*q)]
   if all(4 in u for u in(q[0],q[2],t[0],t[2])):
    for w in r(3):g[c+w][E:E+3]=[x or 7 for x in q[w]]
 return g
