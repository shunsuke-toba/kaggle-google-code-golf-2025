def p(g,k=2,d=0):
 o=g[:k]
 while o[:9]==o:o+=d*[0]+o[-k][:10-d],
 return o if g==o[:len(g)]else p(g,k+(d>1),d+1-(d>1)*3)