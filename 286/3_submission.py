def p(g):
 h=len(g);w=len(g[0]);d=0,1,0,-1;t=sum(g,[]);c=sum({*t}-{0,8});q=[divmod(i,w)for i,v in enumerate(t)if v%8]
 for i,j in q:
  for k in 0,1,2,3:
   x=i+d[k];y=j+d[k-1]
   if h>x>~0<y<w and g[x][y]<1:g[x][y]=c-g[i][j];q+=(x,y),
 return g
