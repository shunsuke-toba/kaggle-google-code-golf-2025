def p(g):
 h=len(g);w=len(g[0]);d=(1,0,-1,0,1);s={*sum(g,[])}-{0,8};a,b=s
 q=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v in s]
 for i,j in q:
  for k in range(4):
   x=i+d[k];y=j+d[k+1]
   if -1<x<h and-1<y<w and g[x][y]==0:g[x][y]=a+b-g[i][j];q+=(x,y),
 return g
