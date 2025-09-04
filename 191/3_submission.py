def p(g,R=range,n=23):
 f=sum(g,[]);i=f.index(1);k=~f[::-1].index(1);m=[(*[x&4for x in r[i%n+1:k%n]],)for r in g[i//n+1:k//n]]
 for _ in R(4):
  h=len(r:=m[::-1]);w=len(r[0])
  for i in R(n*n):k=i%n;i//=n;[(*g[k:k+w],)for g in g[i:i+h]]in(m,r)and[V.insert(U,V.pop(U)or 1)for V in g[i-(i>0):i-~h]for U in R(n)if-2<U-k<w+1]
  m=[*zip(*r)]
 return g