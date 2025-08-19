def p(g,R=range):
 for z in R(999):
  x,y=divmod(z,len(g[0])-2)
  if len(s:={*(l:=sum(p:=[r[x:x+3]for r in g[y:y+3]],[]))})>3:break
 for s in [3,2,1]:
  z=3*s
  r=[[p[i//s][j//s] for j in R(z)] for i in R(z)]
  for _ in R(4):
   for y in R(len(g)-z+1):
    for x in R(len(g[0])-z+1):
     if all((r[i][j] if l.count(r[i][j])==1 else g[-1][0])==g[y+i][x+j] for i in R(z) for j in R(z)):
      for i in R(z): g[y+i][x:x+z]=r[i]
   r=[*zip(*r[::-1])]
 return g