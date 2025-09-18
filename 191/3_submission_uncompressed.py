def p(g,R=range,n=23):
 f=bytes(sum(g,[]));i=f.find(1);k=f.rfind(1);m=[(*[g&4for g in g[i%n+1:k%n]],)for g in g[i//n+1:k//n]]
 for _ in R(4):
  h=len(r:=m[::-1]);w=len(r[0])
  for i in R(n*n):k=i%n;i//=n;[(*g[k:k+w],)for g in g[i:i+h]]in(m,r)and[exec('g[i]=1')for g in g[i-(i>0):i-~h]for i in R(n)if-2<i-k<=w>g[i]]
  m=[*zip(*r)]
 return g