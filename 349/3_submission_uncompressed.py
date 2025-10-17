def p(g):
 x=[r[:]for r in g];n=len(g)
 for l in range(n*n):
  if(u:=g[p:=l//n])[h:=l%n]>g[p-1][h]*p|u[h-1]*h:
   while p<n and g[p][h]:p+=1;d=h
   while d<n and u[d]:d+=1;r=d-h>>1;a=l//n-r-n
   for l in x[p:]:l[h:d]=[1]*(d-h)
   for l,u in zip(x[a:p+r],g[a:]):l[h-r-n:d+r]=[h or 3for h in u[h-r-n:d+r]]
 return x