def p(g):
 next(z for z in range(676)if(q:=[g[(i:=z//26)+k//5][(j:=z%26)+k%5]for k in range(25)])==q[::-1]and len({*q})>2)
 for u in g[i:i+5]:u[j:j+5]=[b:=q[0]]*5;D=1,0,-1,0
 for i,j in[(i,j)for i in range(30)for j in range(30)if g[i][j]==q[12]]:
  for d in range(4):
   v=q[(22,10,2,14)[d]];x=i;y=j
   while v!=b!=g[x][y]:g[x][y]=v;x+=D[d];y+=D[~d]
  for d in range(25):
   v=q[d];x=i-2+d//5;y=j-2+d%5
   if v!=b!=g[x][y]:g[x][y]=v
 return g