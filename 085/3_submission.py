def p(g):
 for a,b in zip(g,g[1:]):
  if a==b:i=a.index(max(a))+1;b[i::2]=[0]*len(b[i::2])
 return g