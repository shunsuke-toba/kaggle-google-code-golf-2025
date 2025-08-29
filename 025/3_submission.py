def p(g):
 t=[*zip(*g)];o=[[0]*len(g)for g in g]
 for x,k in enumerate(t):
  if{*k}=={c:=k[0]}-{0}:
   for r,q in zip(g,o):q[x-(c in r[:x])]=q[x+(c in r[x+1:])]=c
 return any(o[0])and o or tuple(zip(*p(t)))