def p(g):
 n=0
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:
    n+=1
    for R in g[y:y+4]:R[max(x-3,0):x+4]=[0]*7
 return[[0]*i+[8]+[0]*(n+~i)for i in range(n)]