def p(u):
 *n,s=sorted({*sum(u,[])},key=sum(u,[]).count)
 def f(p,t=u):
  while p not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  while p not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  while p not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  while p not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  return [[[s,p][t==p]for t in t]for t in t]
 for p in n:
  for d in n:
   if(p-d)*any(all(f(p)[r+n>>1][u+t>>1]==[s,p][f(d)[n][t]==d]for t in range(len(f(d)[0]))for n in range(len(f(d))))for u in range(len(f(p)[0])*2-len(f(d)[0])+1)for r in range(len(f(p))*2-len(f(d))+1)):return f(p)