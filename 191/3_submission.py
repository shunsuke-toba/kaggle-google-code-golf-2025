def p(g,R=range,n=23):
 f=sum(g,[]);i=f.index(1);k=~f[::-1].index(1);m=[(*[x&4for x in r[i%n+1:k%n]],)for r in g[i//n+1:k//n]]
 for _ in R(4):
  h=len(r:=m[::-1]);w=len(r[0])
  for t in R(529):y=t//n;x=t%n;[(*g[x:x+w],)for g in g[y:y+h]]in(m,r)and[V.insert(U,V.pop(U)or 1)for V in g[y-(y>0):y+h+1]for U in R(x-1,x+w+1)if-1<U<n]
  m=[*zip(*r)]
 return g