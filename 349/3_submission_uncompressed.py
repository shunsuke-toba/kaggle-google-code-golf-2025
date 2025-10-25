def p(g):
 f=[l[:]for l in g];m=len(g)
 for e in range(m):
  for a in range(m):
   if g[e][a]>g[e-1][a]*e|g[e][a-1]*a:
    x=e;d=a
    while d<m and g[e][d]:d+=1
    while x<m and g[x][a]:x+=1;r=d-a>>1
    for l in f[e-r-m:x+r]:l[a-r-m:d+r]=[max(l,3)for l in l[a-r-m:d+r]]
    for l in f[x:]:l[a:d]=[max(l,1)for l in l[a:d]]
 return f
