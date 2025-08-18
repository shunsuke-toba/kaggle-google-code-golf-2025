def p(g,R=range):
 for s in 3,4,5:
  for i in R(13-s):
   for j in R(13-s):
    u=g[i:][:s]
    if u[0][j:j+s]==[5]*s==u[-1][j:j+s]*all(r[j]for r in u):
     for r in u[1:-1]:r[j+1:j+s-1]=[s+3]*(s-2)
 return g