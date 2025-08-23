def p(g):
 h=len(g);w=len(g[0]);t=1,0,-1,0,1
 for i,j in[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]:
  for d,e in zip(t,t[1:]):
   a,b=i,j;y,x=i+d,j+e
   while w>x>-1<y<h>g[y][x]<1:y+=d;x+=e
   if w>x>-1<y<h>7<g[y][x]:
    while(a,b)!=(y,x):a+=d;b+=e;g[a][b]=2
    for m in y-1,y,y+1:g[m][x-1:x+2]=8,8,8;g[y][x]=2
 return g
