def p(g):
 for _ in 0,0:
  for r in g:
   b=99
   for i,x in enumerate(r):
    if x&1:r[b:i]=[8]*(i-b);b=i+1
  g=*map(list,zip(*g)),
 return g