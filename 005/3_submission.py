def p(g):
 R=0,1,2;r=c=0
 while 0in map(sum,(P:=[g[r+i][c:c+3]for i in R])+[*zip(*P)]):c+=1;r+=c>18;c%=19
 for Y in-4,0,4:
  for X in-4,0,4:
   t=max(max(g[r+Y+i][c+X:c+X+3])for i in R);y,x=r,c
   for _ in g:y+=Y;x+=X;[P[i][j]*(0<=y+i<21>x+j>=0)and g[y+i].__setitem__(x+j,t)for i in R for j in R]
 return g