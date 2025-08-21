def p(g):
 d={};r=range
 for i in r(len(g)-2):
  for j in r(len(g[0])-2):
   t=tuple(tuple(r[j:j+3])for r in g[i:i+3])
   if 0 not in[*map(sum,t),*map(sum,zip(*t))]:
    d[t]=d.get(t,0)+1
 return [*map(list,max(d,key=d.get))]
