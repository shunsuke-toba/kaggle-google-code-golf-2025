def p(g):
 h=len(g);w=len(g[0]);s=[(i,j)for i in range(h)for j in range(w)if g[i][j]==3]
 def f(y,x,a,b,t=0):
  y+=a;x+=b
  if not(0<=y<h and 0<=x<w):return
  v=g[y][x]
  if v==2:return[(y-a,x-b)]
  if v<8:r=f(y,x,a,b,t)
  else:
   if t>1:return
   r=f(y-a,x-b,-b,a,t+1)or f(y-a,x-b,b,-a,t+1)
  return r and [(y-a,x-b)]+r
 (y,x),(Y,X)=sorted(s)
 for y,x,a,b in(((y,x,0,-1),(Y,X,0,1)),((y,x,-1,0),(Y,X,1,0)))[y!=Y]:
  if 0<=y+a<h and 0<=x+b<w and g[y+a][x+b]-8:
   r=f(y,x,a,b)
   if r:
    for y,x in r:g[y][x]=3
    break
 return g
