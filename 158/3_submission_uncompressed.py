def p(g,t=0):
 while len({*(f:=sum(p:=[r[t//-~len(g[0]):][:3]for r in g[t%-~len(g[0]):][:3]],[]))})<4:t+=1
 c=f.count
 for _ in range(4):
  for m in 3,2,1:
   for x in range(-~len(g[0])-3*m):
    for y in range(-~len(g)-3*m):
     if all((g[-1][0],p[i//m][j//m])[c(p[i//m][j//m])<2]==g[y+i][x+j]for j in range(3*m)for i in range(3*m)):
      for i in range(3*m):g[y+i][x:x+3*m]=[p[i//m][j//m]for j in range(3*m)]
  p=[*zip(*p[::-1])]
 return g