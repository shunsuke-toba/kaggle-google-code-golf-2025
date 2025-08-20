def p(g):
 o=[[0]*3 for _ in(0,)*3];d=-1,0,1
 for i,r in enumerate(g):
  for j,c in enumerate(r):
   if c==5:
    for x in d:
     for y in d:
      if v:=g[i+x][j+y]:o[x+1][y+1]=v
 return o
