def p(w):
 f=[r[:]for r in w];n=len(w)
 for l in range(n*n):
  if(u:=w[y:=l//n])[a:=l%n]>w[y-1][a]*y|u[a-1]*a:
   while y<n and w[y][a]:y+=1;d=a
   while d<n and u[d]:d+=1;r=d-a>>1;i=l//n-r-n
   for l in f[y:]:l[a:d]=[max(l,1)for l in l[a:d]]
   for l in f[i:y+r]:l[a-r-n:d+r]=[max(l,3)for l in l[a-r-n:d+r]]
 return f