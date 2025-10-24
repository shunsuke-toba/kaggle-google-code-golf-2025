def p(w):
 f=[l[:]for l in w];n=len(w)
 for y in range(n):
  u=w[y]
  for a in range(n):
   if u[a]>w[y-1][a]*y|u[a-1]*a:
    z=y;d=a
    while z<n and w[z][a]:z+=1
    while d<n and u[d]:d+=1;r=d-a>>1
    for l in f[y-r-n:z+r]:l[a-r-n:d+r]=[max(l,3)for l in l[a-r-n:d+r]]
    for l in f[z:]:l[a:d]=[max(l,1)for l in l[a:d]]
 return f