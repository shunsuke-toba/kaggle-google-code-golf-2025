def p(g):
 for _ in[0]*4:
  [set(r)>={2,5}and exec("j=r.index(2);r[j-3:j+4]=0,0,0,2,*r[j-3:j][::-1]")for r in g];g=[*map(list,zip(*g[::-1]))]
 return g