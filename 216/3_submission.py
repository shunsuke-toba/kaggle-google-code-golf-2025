def p(g):
 m=t=0;R=range
 for r in R(20):
  for c in R(20):
   for x in R(r,20):
    for y in R(c,20):
     v=0
     for i in R(r,x+1):
      for j in g[i][c:y+1]:
       if j<1:v=-1;break
       v+=99*j-98
      if v<0:break
     if v>m:m=v;t=r,c,x,y
 r,c,x,y=t;return[g[i][c:y+1]for i in R(r,x+1)]
