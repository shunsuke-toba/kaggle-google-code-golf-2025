def p(g):
 f=[l[:]for l in g];n=len(g)
 for y in range(n):
  for a in range(n):
   if g[y][a]>g[y-1][a]*y|g[y][a-1]*a:
    z=y;d=a
    while d<n and g[y][d]:d+=1
    while z<n and g[z][a]:z+=1;r=d-a>>1
    for l in f[y-r-n:z+r]:l[a-r-n:d+r]=[max(l,3)for l in l[a-r-n:d+r]]
    for l in f[z:]:l[a:d]=[max(l,1)for l in l[a:d]]
 return f