def p(g):
 r=range;d=1,0,-1,0;s=[]
 for n in r(150):
  y=n//15;x=n%15;t=g[y][x]//5*[(0,0)];g[y][x]%=5;s+=t,
  for a,b in t:
   for k in r(4):
    if (u:=y+a+d[k])<10>-1<(v:=x+b+d[~k])<15>g[u][v]>4:g[u][v]=0;t+=(u-y,v-x),
 while s:
  _,t,i,j=min((~sum(i+a<3for a,b in t),t,i,j)for t in s for i in(1,2)for j in r(15)if all(j+b<15>g[i+a][j+b]<1for a,b in t));s.remove(t)
  for a,b in t:g[i+a][j+b]=1
 return g