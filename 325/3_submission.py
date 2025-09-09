def p(g,n=0,e=enumerate):
 for y,r in e(g):
  for x,v in e(r):
   n+=v//8
   for R in g[y:y+v//2]:R[max(x-2,0):x+4]=[0]*6
 return[[0]*i+[8]+[0]*(n+~i)for i in range(n)]