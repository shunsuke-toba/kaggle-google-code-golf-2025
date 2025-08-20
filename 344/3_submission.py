def p(g,e=enumerate):
 for i,r in e(g):
  for k,v in e(r):
   for a,b in(i+1,k),(i,k+1):
    if(len(g)>a)&(b<len(r))and g[a][b]*v==6:r[k],g[a][b]=v%2*8,~v%2*8
 return g
