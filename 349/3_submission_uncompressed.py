def p(w):
 f=[r[:]for r in w];n=len(w)
 for l in range(n*n):
  if(u:=w[p:=l//n])[o:=l%n]>w[p-1][o]*p|u[o-1]*o:
   while p<n and w[p][o]:p+=1;d=o
   while d<n and u[d]:d+=1;r=d-o>>1;a=l//n-r-n
   for l in f[p:]:l[o:d]=[1]*(d-o)
   for l,u in zip(f[a:p+r],w[a:]):l[o-r-n:d+r]=[o or 3for o in u[o-r-n:d+r]]
 return f