def p(g):
 w=[r[:]for r in g];n=len(g)
 for l in range(n*n):
  if(x:=g[a:=l//n])[e:=l%n]>g[a-1][e]*a|x[e-1]*e:
   while a<n and g[a][e]:a+=1;d=e
   while d<n and x[d]:d+=1;r=d-e>>1;i=l//n-r-n
   for l in w[a:]:l[e:d]=[max(l,1)for l in l[e:d]]
   for l in w[i:a+r]:l[e-r-n:d+r]=[max(l,3)for l in l[e-r-n:d+r]]
 return w