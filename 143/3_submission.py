def p(g):
 A=set();d=1,0,-1,0,1
 for z in range(100):
  i=z//10;j=z%10;v=g[i][j]
  if v%5:
   q=[(i,j)];g[i][j]=0
   for x,y in q:
    for k in 0,1,2,3:
     a=x+d[k];b=y+d[k+1]
     if 9>=a>=0<=b<=9 and g[a][b]==v:g[a][b]=0;q+=[(a,b)]
   r,c=zip(*q);s=tuple(sorted((x-min(r),y-min(c))for x,y in q));t=i<4>j;t and A.add(s);v=[v,5][s in A and t^1]
   for x,y in q:g[x][y]=v
 return g
