def p(g):
 for k in 2,3:
  for d in 0,1,2:
   o=g[:k]
   while o[:9]==o:o+=d*[0]+o[-k][:10-d],
   if g==o[:len(g)]:return o