def p(g,r=range):
 for z in r(676):
  i=z//26;j=z%26
  if(q:=[g[i+z//5][j+z%5]for z in r(25)])==q[::-1]and len({*q})>2:b=q[0];break
 for u in g[i:i+5]:u[j:j+5]=[b]*5;D=1,0,-1,0
 for i,j in[(i,j)for i in r(30)for j in r(30)if g[i][j]==q[12]]:
  for d in r(4):
   v=q[(22,10,2,14)[d]];x=i;y=j
   while v!=b!=g[x][y]:g[x][y]=v;x+=D[d];y+=D[d-3]
  for t in r(25):
   if(v:=q[t])!=b!=g[x:=i-2+t//5][y:=j-2+t%5]:g[x][y]=v
 return g