def p(g):
 for _ in[0]*4:
  [exec("j=r.index(2);r[j-3:j+4]=0,0,0,2,*r[j-3:j][::-1]")for r in g if{2,5}<=set(r)];g=[*map(list,zip(*g[::-1]))]
 return g