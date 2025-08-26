def p(g):
 s=[(i//10,i%10)for i in range(100)if sum(g,[])[i]]
 for(a,b),(c,d)in zip(s[::4],s[3::4]):
  for r in g[a+1:c]:r[b+1:d]=[2]*(~b+d)
 return g