R=range
def p(g):
 for y in R(len(g)-4):
  for x in R(len(g[0])-4):
   if sum(g[y+k//5][x+k%5]==1for k in R(25))>15:
    for r in g:r[x+2]=r[x+2]==1 or 6
    g[y+2]=[c==1 or 6 for c in g[y+2]]
 return g
