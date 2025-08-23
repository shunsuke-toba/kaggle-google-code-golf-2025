def p(g,R=range,n=23):
 f=sum(g,[]);i=f.index(1);k=~f[::-1].index(1);m=[[x&4for x in r[i%n+1:k%n]]for r in g[i//n+1:n+k//n]]
 for _ in R(4):
  r=m[::-1];h=len(r);w=len(r[0])
  for y in R(n):
   for x in R(n):
    if[g[x:x+w]for g in g[y:y+h]]in(m,r):
     for V in R(y-1,y+h+1):
      for U in R(x-1,x+w+1):
       if-1<V<n>U>-1:g[V][U]+=g[V][U]<1
  m=[*map(list,zip(*r))]
 return g