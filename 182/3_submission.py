def p(g):
 R=range;h=len(g);d=0,0,1,0
 for z in R((h-6)**2):
  y,x=divmod(z,h-6)
  if all(g[y+d[k]][x+d[k-2]]==5 for k in R(3)):
   t={(i,j)for i in R(5)for j in R(5)if g[y+i+1][x+j+1]>1}
   i,j=next(iter(t));c=g[y+i+1][x+j+1]
 for z in R((h-4)**2):
  y,x=divmod(z,h-4)
  if {(i,j)for i in R(5)for j in R(5)if g[y+i][x+j]==1}==t:
   for i,j in t:g[y+i][x+j]=c
 return g
