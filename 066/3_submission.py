def p(g):
 h=len(g);w=len(g[0]);a=[(i,j)for i in range(h)for j in range(w)if g[i][j]==3]
 (y,x),(Y,X)=sorted(a)
 s=[(y,x,0,-1),(Y,X,0,1)]if y==Y else[(y,x,-1,0),(Y,X,1,0)]
 def f(y,x,dy,dx,t):
  ny=y+dy;nx=x+dx
  if-1<ny<h>-1<nx<w:
   v=g[ny][nx]
   if v==2:return[(y,x)]
   if v==8:
    if t>1:return
    for nd in(-dx,dy),(dx,-dy):
     r=f(y,x,*nd,t+1)
     if r:return[(y,x)]+r
   else:
    r=f(ny,nx,dy,dx,t)
    if r:return[(y,x)]+r
 for y,x,dy,dx in s:
  ny=y+dy;nx=x+dx
  if 0<=ny<h and 0<=nx<w and g[ny][nx]!=8:
   r=f(y,x,dy,dx,0)
   if r:
    for y,x in r:g[y][x]=3
    break
 return g
