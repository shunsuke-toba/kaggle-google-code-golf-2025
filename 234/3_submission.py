def p(g):
 c=n=r=0;N=len(g);M=len(g[0]);d=1,0,-1,0,1
 for i in range(1,N-1):
  for j in range(1,M-1):
   if g[i][j]and((g[i-1][j]==0and g[i+1][j]==0)or(g[i][j-1]==0and g[i][j+1]==0)):c+=1;n=g[i][j];g[i][j]=0;[r:=k for k in range(4)if g[i+d[k]][j+d[k+1]]!=n and g[i+d[k]][j+d[k+1]]]
 I=range(N);J=range(M)
 if r==3:J=range(M-1,-1,-1)
 if r==0:I=range(N-1,-1,-1)
 for i in I:
  for j in J:
   if g[i][j]==n:
    ni,nj=i+d[r]*c,j+d[r+1]*c
    if g[ni][nj]==0:g[ni][nj]=n;g[i][j]=0
 return g