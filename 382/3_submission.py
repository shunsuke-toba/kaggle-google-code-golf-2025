def p(g):
 v=all(r[0]+r[-1]-2 for r in g)
 if v:g=[*map(list,zip(*g))]
 a=2 in[r[-1]for r in g];b=8 in g[-1];g=[r[::1-2*a]for r in g][::1-2*b]
 w=len(g[0]);s=0
 for r in g[1:]:
  s+=r[0]>1
  for j in range(w-s):
   if g[0][j]>7:r[j+s]=8
 g=[r[::1-2*a]for r in g[::1-2*b]]
 if v:g=[*map(list,zip(*g))]
 return g
