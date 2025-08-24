def p(g):
 a,*_,b=[i for i,c in enumerate(zip(*g))if 8 in c]
 for r in g:
  for j in range(a,-~b):r[j]+=8 in r and 2//r[j]
 return g
