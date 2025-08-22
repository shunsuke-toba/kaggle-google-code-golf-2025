def p(g):
 d={};r=range;T=tuple
 for i in r(12):
  for j in r(12):
   t=T(T(r[j:j+3])for r in g[i:i+3])
   if 0not in[*map(sum,t+T(zip(*t)))]:d[t]=d.get(t,0)+1
 return [*map(list,max(d,key=d.get))]
