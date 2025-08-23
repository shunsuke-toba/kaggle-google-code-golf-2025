def p(g):
 x=[i for i,c in enumerate(zip(*g))if 8 in c]
 for r in g:
  if 8 in r:
   for j in range(x[0],-~x[-1]):r[j]+=2//r[j]
 return g
