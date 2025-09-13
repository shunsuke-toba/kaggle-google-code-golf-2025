def p(g,r=range):
 for z in r(676):
  a=[g[(i:=z//26)+k//5][(j:=z%26)+k%5]for k in r(25)]
  if a==a[::-1]and len({*a})>2:break
 b=a[0]
 for k in r(25):g[i+k//5][j+k%5]=b
 d=1,0,-1,0
 s=[(i,j)for z in r(676)if g[(i:=z//26+2)][(j:=z%26+2)]==a[12]]
 for i,j in s:
  for c in r(4):
   v=a[(22,10,2,14)[c]];x=i;y=j
   while v!=b!=g[x][y]:g[x][y]=v;x+=d[c];y+=d[~c]
  for k in r(25):
   if g[i-2+k//5][j-2+k%5]!=b!=a[k]:g[i-2+k//5][j-2+k%5]=a[k]
 return g
