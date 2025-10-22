def p(r):
 t=23;q=bytes(sum(r,[]));i=q.find(1);e=q.rfind(1);u=[(*[r&4for r in r[i%t+1:e%t]],)for r in r[i//t+1:e//t]]
 for i in range(4):
  for i in range(t*t):
   e=i%t;i//=t
   [(*[r&4for r in r[e:e+len(u[0])]],)for r in r[i:i+len(u)]]in(u,u[::-1])and[exec('r[i]=1')for r in r[i-(i>0):i-~len(u)]for i in range(t)if-2<i-e<=len(u[0])>r[i]]
  u=[*zip(*u[::-1])]
 return r