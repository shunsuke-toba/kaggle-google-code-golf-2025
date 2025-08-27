def p(g):
 r=range;d=1,0,-1,0,1;s=[]
 for I in r(10):
  for J in r(15):
   if g[I][J]>4:
    t=[(0,0)];g[I][J]=0
    for y,x in t:
     for k in r(4):
      u=I+y+d[k];v=J+x+d[k+1]
      if 15>v>-1<u<10>g[u][v]>4:g[u][v]=0;t+=(u-I,v-J),
    s+=t,
 while s:
  t,I,J=max(((t,I,J)for t in s for I in(1,2)for J in r(15)if all(15>J+x and g[I+y][J+x]<1 for y,x in t)),key=lambda q:sum(q[1]+y<3 for y,x in q[0]))
  for y,x in t:g[I+y][J+x]=1
  s.remove(t)
 return g
