def p(r):
 t=23;h=bytes(sum(r,[]));i=h.find(1);f=h.rfind(1);u=[(*[r&4for r in r[i%t+1:f%t]],)for r in r[i//t+1:f//t]];print(u)
 for i in range(4):
  for i in range(t*t):
   f=i%t;i//=t
   [(*[r&4for r in r[f:f+len(u[0])]],)for r in r[i:i+len(u)]]in(u,u[::-1])and[exec('r[i]=1')for r in r[i-(i>0):i-~len(u)]for i in range(t)if-2<i-f<=len(u[0])>r[i]]
  u=[*zip(*u[::-1])]
 return r