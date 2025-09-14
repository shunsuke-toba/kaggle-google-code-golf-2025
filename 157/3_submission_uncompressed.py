def p(g):
 d=1,0,-1,0;s=[]
 for i in range(10):
  for j in range(15):
   t=g[i][j]//5*[(0,0)];g[i][j]%=5;s+=t,
   for a,b in t:
    for k in range(4):
     if(u:=i+a+d[k])<10>-1<(v:=j+b+d[~k])<15>g[u][v]>4:g[u][v]=0;t+=(u-i,v-j),
 while s:
  _,t,i,j=min((~sum(i+a<3for a,b in t),t,i,j)for t in s for i in(1,2)for j in range(15)if all(j+b<15>g[i+a][j+b]<1for a,b in t));s.remove(t)
  for a,b in t:g[i+a][j+b]=1
 return g
