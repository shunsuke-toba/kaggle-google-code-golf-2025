def p(g,R=range,n=23):
 f=bytes(sum(g,[]));i=f.find(1);k=f.rfind(1);m=[(*[x&4for x in r[i%n+1:k%n]],)for r in g[i//n+1:k//n]]
 for _ in R(4):
  h=len(r:=m[::-1]);w=len(r[0])
  for i in R(n*n):k=i%n;i//=n;[(*g[k:k+w],)for g in g[i:i+h]]in(m,r)and[exec('V[U]+=1>V[U]')for V in g[i-(i>0):i-~h]for U in R(n)if-2<U-k<=w]
  m=[*zip(*r)]
 return g