def p(g):
 L=len;h=L(g);w=L(g[0]);R=range;F=filter;S=[]
 for y in R(h):
  for x in R(w):
   q,a,b=[],y,x
   for s in R(y+1,h+1):
    for t in R(x+1,w+1):
     if (m:=[g[i][x:t] for i in R(y,s)])==[*map(list,zip(*F(any,zip(*F(any,m)))))]and L({0,*sum(m,[])})>4:q,a,b=m,s,t
   if q:S+=q,
   for i in R(y,a):g[i][x:b]=[0]*(b-x)
 for r in S:
  for z in R(8):
   a=L(r);b=L(r[0]);u=sum(r,[])
   for y in R(h-a+1):
    for x in R(w-b+1):
     if all(r[i][j]*(u.count(r[i][j])==1)==g[y+i][x+j]for i in R(a)for j in R(b)):
      for i in R(a):g[y+i][x:x+b]=r[i]
   r=[list(t)for t in zip(*r[::-1])]
   if z&3>2:r=r[::-1]
 return g
