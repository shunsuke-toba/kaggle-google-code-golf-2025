def p(g):
 for r in g:
  for c in range(10):
   if r[c]==5:
    d=c
    while d<10>r[d]==5:d+=1
    r[c:d]=[max(g[0][c:d])]*(d-c)
 return g
