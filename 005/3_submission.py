def p(g):
 H=len(g)-2;W=len(g[0])-2;R=range(3);r=c=0
 while 0 in map(sum,(P:=[g[r+i][c:c+3]for i in R])+[*zip(*P)]):
  c+=1;r+=c//W;c%=W
 for Y in-4,0,4:
  for X in-4,0,4:
   y=r+Y;x=c+X
   if X|Y and-1<y<H and-1<x<W:
    t=max(max(g[y+i][x:x+3])for i in R);yy=r;xx=c
    while t:
     yy+=Y;xx+=X
     for i in R:
      for j in R:
       if P[i][j]and-1<yy+i<H+2and-1<xx+j<W+2:g[yy+i][xx+j]=t
     if(-1<yy<H)*(-1<xx<W)<1:break
 return g
