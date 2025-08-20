def p(g):
 s={(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==2}
 while s:
  t=[s.pop()];c=[]
  while t:
   y,x=t.pop();c+=[(y,x)]
   for u in range(y-2,y+3):
    for v in range(x-2,x+3):
     if(u,v)in s:s.remove((u,v));t+=[(u,v)]
  U,V=zip(*c)
  for r in g[min(U):max(U)+1]:
   for x in range(min(V),max(V)+1):
    if r[x]-2:r[x]=4
 return g
