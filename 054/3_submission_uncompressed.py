def p(g,R=range):
 for z in R(676):
  q=[g[(i:=z//26)+k//5][(j:=z%26)+k%5]for k in R(25)]
  if q==q[::-1]and len({*q})>2:break
 o=q[0]
 for k in R(25):g[i+k//5][j+k%5]=o
 D=1,0,-1,0
 S=[(i,j)for z in R(676)if g[(i:=z//26+2)][(j:=z%26+2)]==q[12]]
 for i,j in S:
  for d in R(4):
   v=q[(22,10,2,14)[d]];x=i;y=j
   while v!=o!=g[x][y]:g[x][y]=v;x+=D[d];y+=D[~d]
  for k in R(25):
   if g[i-2+k//5][j-2+k%5]!=o!=q[k]:g[i-2+k//5][j-2+k%5]=q[k]
 return g
