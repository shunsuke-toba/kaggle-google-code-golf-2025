def p(g,e=enumerate):
 for i,r in e(g):
  for k,v in e(r):
   for a,b in(i+1,k),(i,k+1):
    try:
     if g[a][b]*v==6:r[k],g[a][b]=v%2*8,~v%2*8
    except:0
 return g