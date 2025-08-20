def p(g):
 c=[0]*10;l=[9]*10
 for r in g:
  for x,v in enumerate(r):
   if v:c[v]+=1;l[v]=min(l[v],x)
 m=max(c)
 return[[i for x,i in sorted((l[i],i)for i in range(10)if c[i]==m)]]*m
