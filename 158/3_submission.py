def p(g,R=range):
 W=len(g[0])-2;t=0
 while len({*(p:=sum([r[t//W:][:3]for r in g[t%W:][:3]],[]))})<4:t+=1
 for s in 3,2,1:
  u=R(z:=3*s);r=[[p[i//s*3+j//s]for j in u]for i in u]
  for _ in R(4):
   for y in R(len(g)+1-z):
    for x in R(W+3-z):
     if all((g[-1][0],r[i][j])[p.count(r[i][j])<2]==g[y+i][x+j]for i in u for j in u):
      for i in u:g[y+i][x:x+z]=r[i]
   r=[*zip(*r[::-1])]
 return g