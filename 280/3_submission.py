def p(g):
 h=len(g);w=len(g[0])
 for r,c in[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]:
  u=r
  while u and g[u-1][c]>2:u-=1
  d=r
  while d+1<h and g[d+1][c]>2:d+=1
  l=c
  while l and g[r][l-1]>2:l-=1
  e=c
  while e+1<w and g[r][e+1]>2:e+=1
  for dx,dy in(-1,0),(1,0),(0,-1),(0,1):
   x=r+dx;y=c+dy
   if x<0 or y<0 or x>=h or y>=w or g[x][y]<1:
    s=(d-u,e-l)[dx==0];L=(l,u)[dx==0];R=(e,d)[dx==0];C=(c,r)[dx==0]
    for i in range(max(L,C-s),min(R,C+s)+1):
     x,y=(r,i)if dx else(i,c);v=g[x][y]
     while 0<=x<h and 0<=y<w:g[x][y]=v;x+=dx;y+=dy
    break
 return g
