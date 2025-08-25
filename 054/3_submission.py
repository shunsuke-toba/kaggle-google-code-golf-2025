def p(g,R=range):
 b=g[0][0];D=1,0,-1,0
 for z in R(676):
  i,j=divmod(z,26);q=sum((r[j:j+5]for r in g[i:i+5]),[])
  if q==q[::-1]and len({*q})>2:break
 for r in g[i:i+5]:r[j:j+5]=[b]*5
 s=[(i,j)for i in R(30)for j in R(30)if g[i][j]==q[12]]
 for i,j in s:
  for d in R(4):
   v=q[(22,10,2,14)[d]];x=i;y=j
   while v^b and g[x][y]^b:g[x][y]=v;x+=D[d];y+=D[d-3]
  for t in R(25):
   v=q[t];x=i+t//5-2;y=j+t%5-2
   if v^b and g[x][y]^b:g[x][y]=v
 return g
