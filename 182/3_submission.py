def p(g):
 R=range;h=len(g)
 for y in R(h-6):
  for x in R(h-6):
   if all(g[y+i][x+j]==5 for i in R(7)for j in R(7)if i in(0,6)or j in(0,6)):
    t={(i,j)for i in R(5)for j in R(5)if g[y+i+1][x+j+1]>1}
    i,j=next(iter(t));c=g[y+i+1][x+j+1]
    for y in R(h-4):
     for x in R(h-4):
      if {(i,j)for i in R(5)for j in R(5)if g[y+i][x+j]==1}==t:
       for i,j in t:g[y+i][x+j]=c
    return g
