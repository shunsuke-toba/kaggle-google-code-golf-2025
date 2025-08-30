def p(g,R=range):
 w=len(g[0])-2;t=0
 while len({*(p:=sum((r[t//w:][:3]for r in g[t%w:][:3]),[]))})<4:t+=1
 for m in 3,2,1:
  q=R(s:=3*m);a=[[p[i//m*3+j//m]for j in q]for i in q]
  for _ in R(4):
   for y in R(len(g)+1-s):
    for x in R(w+3-s):
     if all((g[-1][0],v:=a[i][j])[p.count(v)<2]==g[y+i][x+j]for i in q for j in q):
      for i in q:g[y+i][x:x+s]=a[i]
   a=[*zip(*a[::-1])]
 return g