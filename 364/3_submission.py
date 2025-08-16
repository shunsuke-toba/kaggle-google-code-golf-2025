def p(g):
 h=len(g);w=len(g[0]);V=(1,0,-1,0,1)
 for i in range(h):
  for j in range(w):
   if g[i][j]==3:
    s=[(i,j)];g[i][j]=0
    for x,y in s:
     for k in range(4):
      a=x+V[k];b=y+V[k+1]
      if 0<=a<h and 0<=b<w and g[a][b]==3:g[a][b]=0;s+=[(a,b)]
    S={*s};t=m=0
    for x,y in s:
     a=(x+1,y)in S;b=(x-1,y)in S;c=(x,y+1)in S;d=(x,y-1)in S;e=a+b+c+d
     m+=e>2;t+=e==2 and(a^b)&(c^d)
    n=m and 2 or[1,6][t>1]
    for x,y in s:g[x][y]=n
 return g
