def p(g):
 h=len(g);w=len(g[0]);k=sum(g,[]).index(2);i=k//w;j=k%w;q=[(i,j)]
 for x,y in q:
  if g[x][y]==2 and (abs(x-i)>2 or abs(y-j)>2):return[[8]]
  g[x][y]=0
  for a,b in((1,0),(0,1),(-1,0),(0,-1)):
   nx,ny=x+a,y+b
   if 0<=nx<h and 0<=ny<w and g[nx][ny]:q+=[(nx,ny)]
 return[[0]]
