def p(g):
 s={divmod(i,10)for i,v in enumerate(sum(g,[]))if v}
 for a,b in s:
  for c,d in s:
   for r in g[a+1:c]*({(a,d),(c,b)}<=s):r[b+1:d]=[2]*(~b+d)
 return g