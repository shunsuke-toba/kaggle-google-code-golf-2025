def p(g):
 s={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4}
 for a,b in s:
  for c,d in s:
   if{(a,d),(c,b)}<=s:
    for i in range(a+1,c):g[i][b+1:d]=[2]*(~b+d)
 return g
