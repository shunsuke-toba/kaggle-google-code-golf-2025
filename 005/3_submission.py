def p(g):
 n=len(g);N=n-2;R=0,1,2;r=c=0
 while 0 in map(sum,(P:=[g[r+i][c:c+3]for i in R])+[*zip(*P)]):
  c+=1;r+=c//N;c%=N
 for Y in-4,0,4:
  for X in-4,0,4:
   t=(X|Y)and max(max(g[r+Y+i][c+X:c+X+3])for i in R);y,x=r,c
   while t:
    y+=Y;x+=X
    for i in R:
     for j in R:
      if P[i][j]*(n>y+i>-1)*(n>x+j>-1):g[y+i][x+j]=t
    if(-1<y<N)*(-1<x<N)<1:break
 return g
