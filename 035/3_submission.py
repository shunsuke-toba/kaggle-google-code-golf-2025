def p(g):
 l=g[3].index(8);b=2+sum(8in r for r in g)
 for k,x in enumerate(sum(g,[])):
  if x&7:g[max(min(k//10,b),3)][max(min(k%10,5),l)]=x
 return g