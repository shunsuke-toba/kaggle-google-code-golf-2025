def p(g):
 c=n=r=0;N,M=len(g),len(g[0]);d=1,0,-1,0,1;R=range
 for i in R(1,N-1):
  for j in R(1,M-1):
   if(m:=g[i][j])and(g[i-1][j]|g[i+1][j])*(g[i][j-1]|g[i][j+1])<1:c+=1;n=m;g[i][j]=0;[r:=k for k in R(4)if(v:=g[i+d[k]][j+d[k+1]])*(v-n)]
 for i in R(N)[::r>0 or-1]:
  for j in R(M)[::r<3 or-1]:
   if g[i][j]==n>g[a:=i+d[r]*c][b:=j+d[r+1]*c]:g[a][b]=n;g[i][j]=0
 return g
