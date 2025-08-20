def p(g):
 o=[*map(list,g)];h=len(g);w=len(g[0]);d=[(i//3-1,i%3-1)for i in range(9)if i-4]
 for k in range(h*w):
  i=k//w;j=k%w
  if(c:=o[i][j])>0:
   q=[(i,j)];A=[c];o[i][j]=-c
   for y,x in q:
    for a,b in d:
     Y=y+a;X=x+b
     if-1<Y<h>-1<X<w and(c:=o[Y][X])>0:o[Y][X]=-c;q+=(Y,X),;A+=c,
   m=max(A,key=A.count)
   for(y,x),v in zip(q,A):
    if v==m and any(-1<y+a<h and -1<x+b<w and 0<(c:=abs(o[y+a][x+b]))!=m for a,b in d if a*b==0):break
   P=[(r-y,c-x)for(r,c),v in zip(q,A)if v==m]
   for a,b in d:
    Y,X=y+a,x+b
    if-1<Y<h>-1<X<w and 0<(c:=abs(o[Y][X]))!=m:
     for oy,ox in P:
      ty=Y+(a and-oy or oy);tx=X+(b and-ox or ox)
      if-1<ty<h>-1<tx<w:g[ty][tx]=c
 return g
