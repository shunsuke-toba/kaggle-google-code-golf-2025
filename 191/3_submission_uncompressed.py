def p(y):
 n=23;r=bytes(sum(y,[]));i=r.find(1);e=r.rfind(1);m=[(*[y&4for y in y[i%n+1:e%n]],)for y in y[i//n+1:e//n]]
 for _ in range(4):
  for i in range(n*n):
   e=i%n;i//=n
   [(*[y&4for y in y[e:e+len(m[0])]],)for y in y[i:i+len(m)]]in(m,m[::-1])and[exec('y[i]=1')for y in y[i-(i>0):i-~len(m)]for i in range(n)if-2<i-e<=len(m[0])>y[i]]
  m=[*zip(*m[::-1])]
 return y