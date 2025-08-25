def p(g):
 s=[divmod(i,10)for i,v in enumerate(sum(g,[]))if v]
 for(a,b),(c,d)in zip(s[::4],s[3::4]):
  for r in g[a+1:c]:r[b+1:d]=[2]*(~b+d)
 return g
