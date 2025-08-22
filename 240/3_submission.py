def p(g):
 c=[0]*10
 for d in range(9):
  for r in g:
   for v in r[d],r[~d]:
    c[v]+=v>0
    if c[v]>1:r[d:19-d:2]=[v]*(10-d)
 for i in range(19):
  for j in range(19):
   if v:=g[i][j]:g[j][~i]=g[~i][~j]=g[~j][i]=v
 return g
