def p(g):
 h=len(g);w=len(g[0]);s=h*w;v=[0]*s
 for i in range(s):
  c=g[i//w][i%w]
  if c^9 and not v[i]:
   m=[i];v[i]=1;e=0
   for z in m:
    for n in z-1,z+1,z-w,z+w:
     if 0<=n<s and-2<n%w-z%w<2 and g[n//w][n%w]==c:
      e+=1
      if not v[n]:v[n]=1;m+=n,
   if e>=2*len(m):
    for z in m:g[z//w][z%w]=8
 return g
