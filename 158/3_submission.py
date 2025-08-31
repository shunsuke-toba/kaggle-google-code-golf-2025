def p(g,r=range):
 w=len(g[0])-2;t=0
 while len({*(f:=sum(p:=[R[t//w:][:3]for R in g[t%w:][:3]],[]))})<4:t+=1
 for _ in r(4):
  for m in 3,2,1:
   q=r(s:=3*m)
   for y in r(len(g)+1-s):
    for x in r(w+3-s):
     if all((g[-1][0],v:=p[i//m][j//m])[f.count(v)<2]==g[y+i][x+j]for i in q for j in q):
      for i in q:g[y+i][x:x+s]=[p[i//m][j//m]for j in q]
  p=[*zip(*p[::-1])]
 return g