def p(g):
 t=2 in g[0]+g[-1]
 if t:g=[*map(list,zip(*g))]
 A,B=1-2*(2 in(r[-1]for r in g)),1-2*(8 in g[-1]);g=[r[::A]for r in g][::B];s=0
 for r in g[1:]:
  s+=r[0]>1;r[s:]=[x|y for x,y in zip(r[s:],g[0])]
 g=[r[::A]for r in g][::B]
 return[*map(list,zip(*g))]if t else g
