def p(j):
 for i,r in enumerate(j):r[i]=r[~i]=0
 return j
