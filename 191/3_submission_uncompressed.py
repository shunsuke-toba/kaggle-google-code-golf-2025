def p(y,p=range):
 n=23;r=bytes(sum(y,[]));i=r.find(1);e=r.rfind(1);m=[(*[y&4for y in y[i%n+1:e%n]],)for y in y[i//n+1:e//n]]
 for c in p(4):
  f=len(m);r=len(m[0])
  for i in p(n*n):
   e=i%n;i//=n
   [(*[y&4for y in y[e:e+r]],)for y in y[i:i+f]]in(m,m[::-1])and[exec('y[i]=1')for y in y[i-(i>0):i-~f]for i in p(n)if-2<i-e<=r>y[i]]
  m=[*zip(*m[::-1])]
 return y