def p(g):
 q=range(n:=len(g));s=0
 while s<n:
  s+=1;d={}
  if all((v:=g[i][j])<1 or d.setdefault((i%s,j%s),v)==v for j in q for i in q):
   return[[d[i%s,j%s]for j in q]for i in q]
