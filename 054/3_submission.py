def p(g,r=range):
 D=1,0,-1,0
 for z in r(676):
  i=z//26;j=z%26;q=sum((g[i+k][j:j+5]for k in r(5)),[])
  if q==q[::-1]and len({*q})>2:b=q[0];break
 for h in g[i:i+5]:h[j:j+5]=[b]*5
 for i,j in[(i,j)for i in r(30)for j in r(30)if g[i][j]==q[12]]:
  for d in r(4):
   v=q[(22,10,2,14)[d]];x=i;y=j
   while(v^b)*(g[x][y]^b):g[x][y]=v;x+=D[d];y+=D[d-3]
  for t in r(25):
   v=q[t];x=i-2+t//5;y=j-2+t%5
   if v!=b!=g[x][y]:g[x][y]=v
 return g