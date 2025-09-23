def p(g,r=range):
 n=23;f=bytes(sum(g,[]));i=f.find(1);k=f.rfind(1);m=[(*[g&4for g in g[i%n+1:k%n]],)for g in g[i//n+1:k//n]]
 for _ in r(4):
  h=len(m);w=len(m[0])
  for i in r(n*n):
   k=i%n;i//=n
   [(*[g&4for g in g[k:k+w]],)for g in g[i:i+h]]in(m,m[::-1])and[exec('g[i]=1')for g in g[i-(i>0):i-~h]for i in r(n)if-2<i-k<=w>g[i]]
  m=[*zip(*m[::-1])]
 return g