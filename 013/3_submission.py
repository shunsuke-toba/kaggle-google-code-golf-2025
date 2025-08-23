def p(g,R=range):
 h=len(g);w=len(g[0]);(x,y,a),(X,Y,b)=[(i,j,v)for i in R(h)for j in R(w)if(v:=g[i][j])]
 if{x,X}<={0,h-1}:
  if y>Y:y,Y,a,b=Y,y,b,a
  d=Y-y
  for r in g:r[y::d]=([a,b]*9)[:(w-y+d-1)//d]
 else:
  for r in R(x,h,X-x):g[r]=[a]*w;a,b=b,a
 return g
