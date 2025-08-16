def p(g,R=range):
 h=len(g);w=len(g[0])
 (x,y,a),(X,Y,b)=[(i,j,g[i][j])for i in R(h)for j in R(w)if g[i][j]]
 if x==X or{x,X}=={0,h-1}:
  if y>Y:y,Y,a,b=Y,y,b,a
  s=Y-y;C=a,b
  for c in R(y,w,s):
   for r in g:r[c]=C[(c-y)//s&1]
 else:
  s=X-x;C=a,b
  for r in R(x,h,s):g[r]=[C[(r-x)//s&1]]*w
 return g
