def p(g,R=range):
 s=sum(g,[]);b=s[0];D=1,0,-1,0;I=22,10,2,14
 for z in R(676):
  i=z//26;j=z%26;q=sum((r[j:j+5]for r in g[i:i+5]),[])
  if q==q[::-1]and len({*q})>2:break
 for r in g[i:i+5]:r[j:j+5]=[b]*5
 c=q[12]
 for i,j in[(i,j)for i in R(30)for j in R(30)if g[i][j]==c]:
  for t in R(25):
   v=q[t];x=i+t//5-2;y=j+t%5-2
   if g[x][y]!=b!=v:g[x][y]=v
  for d in R(4):
   v=q[I[d]];x=i+D[d]*2;y=j+D[d-3]*2
   if v-b:
    while g[x][y]-b:g[x][y]=v;x+=D[d];y+=D[d-3]
 return g
