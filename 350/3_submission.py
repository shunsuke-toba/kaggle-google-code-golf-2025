def p(g,t=0):
 for r in g:
  b=99;i=0
  for x in r:
   if x&1:r[b:i]=[8]*(i-b);b=-~i
   i+=1
 *g,=map(list,zip(*g))
 return t*g or p(g,1)