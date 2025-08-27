def p(g):
 r=range;d=1,0,-1,0,1;s=[];C=r(15)
 for y in r(10):
  for x in C:
   if g[y][x]>4:
    t=[(0,0)];g[y][x]=0
    for a,b in t:
     for k in r(4):
      u=y+a+d[k];v=x+b+d[k+1]
      if 15>v>-1<u<10>g[u][v]>4:g[u][v]=0;t+=(u-y,v-x),
    s+=t,
 while s:
  _,k,i,j=min((-sum(i+a<3 for a,b in s[k]),k,i,j)for k in r(len(s))for i in(1,2)for j in C if all(0<=j+b<15 and g[i+a][j+b]<1 for a,b in s[k]))
  for a,b in s.pop(k):g[i+a][j+b]=1
 return g
