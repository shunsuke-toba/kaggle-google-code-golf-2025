def p(g,r=range):
 next(z for z in r(676)if(q:=[g[(i:=z//26)+k//5][(j:=z%26)+k%5]for k in r(25)])==q[::-1]and len({*q})>2)
 for u in g[i:i+5]:u[j:j+5]=[b:=q[0]]*5;D=1,0,-1,0
 for i,j in[(i,j)for i in r(30)for j in r(30)if g[i][j]==q[12]]:
  for d in r(4):
   v=q[(22,10,2,14)[d]];x=i;y=j
   while v!=b!=g[x][y]:g[x][y]=v;x+=D[d];y+=D[~d]
  for t in r(25):
   if(v:=q[t])!=b!=g[x:=i-2+t//5][y:=j-2+t%5]:g[x][y]=v
 return g