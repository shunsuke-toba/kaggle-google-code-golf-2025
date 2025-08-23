def p(g,R=range):
 for t in R(999):
  x,y=divmod(t,len(g[0])-2);l=sum(p:=[r[x:x+3]for r in g[y:y+3]],[])
  if len({*l})>3:break
 for s in 3,2,1:
  z=3*s;u=R(z);r=[[p[i//s][j//s]for j in u]for i in u]
  for _ in R(4):
   for y in R(len(g)+1-z):
    for x in R(len(g[0])+1-z):
     if all((g[-1][0],r[i][j])[l.count(r[i][j])==1]==g[y+i][x+j]for i in u for j in u):
      for i in u:g[y+i][x:x+z]=r[i]
   r=[*zip(*r[::-1])]
 return g
