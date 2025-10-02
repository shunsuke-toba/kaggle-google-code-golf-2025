def p(g):
 for a in g*2:
  for b in g:
   for i in range(21):a[i]|=(a[i-3]==b[i-3]>0)*b[i]
 return eval(str(g).replace(*'08'))