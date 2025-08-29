def p(g):
 l=g[3].index(8)
 for k,x in enumerate(sum(g,[])):
  if x&7:g[min(g.index(g[1],3)-1,k//10 or 3)][min(5,k%10)or l]=x
 return g