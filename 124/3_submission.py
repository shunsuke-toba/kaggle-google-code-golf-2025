def p(g):
 for k in 2,3:
  for d in 0,1,2:
   o=g[:k]
   while len(o)<10:o+=d*[0]+o[-k][:10-d],
   if o[:len(g)]==g:return o