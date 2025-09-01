def p(g,i=0):
 k=2+i//3;o=g[:k]
 while o[:9]==o:o+=i%3*[0]+o[-k][:10-i%3],
 return g==o[:len(g)]and o or p(g,i+1)