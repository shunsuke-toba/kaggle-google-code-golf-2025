def p(g):
 H=W=len(g)-2;R=0,1,2;r=c=0
 while 0 in map(sum,(P:=[g[r+i][c:c+3]for i in R])+[*zip(*P)]):
  c+=1;r+=c//W;c%=W
 for Y in-4,0,4:
  for X in-4,0,4:
   if(X|Y)*(-1<r+Y<H)*(-1<c+X<W):
    t=max(max(g[r+Y+i][c+X:c+X+3])for i in R);y,x=r,c
    while t:
     y+=Y;x+=X
     for i in R:
      for j in R:
       if P[i][j]and-1<y+i<H+2and-1<x+j<W+2:g[y+i][x+j]=t
     if(-1<y<H)*(-1<x<W)<1:break
 return g
