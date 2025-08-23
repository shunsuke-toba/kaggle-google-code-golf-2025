def p(g,R=range):
 h=len(g);w=len(g[0]);(x,y,a),(X,Y,b)=[(i,j,v)for i in R(h)for j in R(w)if(v:=g[i][j])]
 if{x,X}<={0,h-1}:
  if y>Y:y,Y,a,b=Y,y,b,a
  for c in R(y,w,Y-y):
   for r in g:r[c]=a
   a,b=b,a
 else:
  for r in R(x,h,X-x):g[r]=[a]*w;a,b=b,a
 return g
