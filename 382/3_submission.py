def p(g):
 v=2 in{r[0]+r[-1]for r in g}
 if not v:g=[*map(list,zip(*g))]
 a=2 in[r[-1]for r in g];b=8 in g[-1]
 if a:g=[r[::-1]for r in g]
 if b:g=g[::-1]
 w=len(g[0])
 t=[i for i in range(w)if 7<g[0][i]];s=0
 for i in range(1,len(g)):
  s+=g[i][0]>1
  for j in t:
   if j+s<w:g[i][j+s]=8
 if b:g=g[::-1]
 if a:g=[r[::-1]for r in g]
 if not v:g=[*map(list,zip(*g))]
 return g
