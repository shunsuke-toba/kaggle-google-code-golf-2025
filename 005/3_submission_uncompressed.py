def p(g):
 R=0,1,2;r=c=0
 while 0in map(sum,(P:=[[g[r+i][c+j]for j in R]for i in R])+[*zip(*P)]):
  c=-~c%19
  r+=c<1
 for Y in-4,0,4:
  for X in-4,0,4:
   y,x=r,c;v=max(g[r+Y+i][c+X+j]for i in R for j in R)
   for _ in g:
    y+=Y;x+=X
    for i in R:
     for j in R:
      if 0<=y+i<21>j+x>=0<P[i][j]:g[y+i][x+j]=v
 return g