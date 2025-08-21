def p(g):
 h=len(g);w=len(g[0]);a=[(i,j)for i in range(h)for j in range(w)if g[i][j]==3]
 def f(y,x,a,b,t):
  Y=y+a;X=x+b
  if-1<Y<h>-1<X<w:
   v=g[Y][X]
   if v==2:return[(y,x)]
   if v==8:
    if t>1:return
    for d in(-b,a),(b,-a):
     r=f(y,x,*d,t+1)
     if r:return[(y,x)]+r
   else:
    r=f(Y,X,a,b,t)
    if r:return[(y,x)]+r
 (y,x),(Y,X)=sorted(a)
 for y,x,a,b in([(y,x,0,-1),(Y,X,0,1)]if y==Y else[(y,x,-1,0),(Y,X,1,0)]):
  Y=y+a;X=x+b
  if-1<Y<h>-1<X<w and g[Y][X]-8:
   r=f(y,x,a,b,0)
   if r:
    for y,x in r:g[y][x]=3
    return g
 return g
