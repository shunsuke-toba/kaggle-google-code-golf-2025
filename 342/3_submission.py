def p(g):
 r,c=divmod(sum(g,[]).index(8),10)
 for q in range(100):
  d=q%10;q//=10;v=g[q][d];g[q][d]=0
  if v&7:g[r+(q>r)][c+(d>c)]=v
 return g