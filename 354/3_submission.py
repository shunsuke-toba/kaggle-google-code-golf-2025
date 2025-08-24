def p(g):
 for r in g:
  while 5 in r:
   b=a=r.index(5)
   while b<10>r[b]==5:b+=1
   r[a:b]=[max(g[0][a:b])]*(b-a)
 return g
