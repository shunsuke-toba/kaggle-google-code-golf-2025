def p(g):
 s=[(i//10,i%10)for i in range(100)if sum(g,[])[i]]
 while s:
  a,b=s[0];c,d=s[3];s=s[4:]
  for r in g[a+1:c]:r[b+1:d]=[2]*(~b+d)
 return g