def p(g):
 l=g[3].index(8)
 for k,x in enumerate(sum(g,[])):
  if x&7:g[max(min(k//10,g.index([0]*10,3)-1),3)][max(min(k%10,5),l)]=x
 return g