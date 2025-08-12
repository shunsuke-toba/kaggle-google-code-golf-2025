def p(g):
 R,C=len(g),len(g[0])
 r=c=-1
 for i in range(R):
  for j in range(C):
   if i+2<R and j+2<C:
    if all(any(g[i+x][j+y]for y in range(3))for x in range(3))and all(any(g[i+x][j+y]for x in range(3))for y in range(3)):
     r,c=i,j;break
  if r!=-1:break
 for dr,dc in[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
  x,y=r+dr*4,c+dc*4
  if 0<=x<R-2 and 0<=y<C-2:
   col=-1
   for i in range(3):
    for j in range(3):
     if g[x+i][y+j]:col=g[x+i][y+j];break
    if col!=-1:break
   if col!=-1:
    s=1
    while 1:
     tx,ty=r+dr*4*s,c+dc*4*s
     for i in range(3):
      for j in range(3):
       if 0<=tx+i<R and 0<=ty+j<C and g[r+i][c+j]:g[tx+i][ty+j]=col
     if tx<0 or tx+2>=R or ty<0 or ty+2>=C:break
     s+=1
 return g