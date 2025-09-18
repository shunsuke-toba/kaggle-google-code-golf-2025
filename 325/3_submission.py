def p(g):
 n=y=0
 for r in g:
  while 8in r:
   n+=1;x=r.index(8)
   for R in g[y:y+4]:R[x-2*(x>1):x+4]=[0]*6
  y+=1
 return[[0]*i+[8]+[0]*(n+~i)for i in range(n)]