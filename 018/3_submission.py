def p(g):
 l=len;h=l(g);w=l(g[0]);R=range;f=filter;S=[]
 for y in R(h):
  for x in R(w):
   a=b=0
   for s in R(y+1,h+1):
    for t in R(x+1,w+1):
     if (m:=[g[i][x:t]for i in R(y,s)])==[*map(list,zip(*f(any,zip(*f(any,m)))))]and l({0,*sum(m,[])})>4:a,b,M=s,t,m
   if a:S+=M,
   for r in g[y:a]:r[x:b]=[0]*(b-x)
 for r in S:
  u=sum(r,[])
  for z in R(8):
   a=l(r);b=l(r[0])
   for y in R(h-a+1):
    for x in R(w-b+1):
     if all(r[i][j]*(u.count(r[i][j])<2)==g[y+i][x+j]for i in R(a)for j in R(b)):
      for i in R(a):g[y+i][x:x+b]=r[i]
   r=[*zip(*r[::-1])]
   if z&3>2:r=r[::-1]
 return g
