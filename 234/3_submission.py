def p(g):
 c=n=k=0;N=len(g);M=len(g[0]);d=1,0,-1,0,1;r=range
 for i in r(N):
  for j in r(M):
   if(m:=g[i][j])and(g[i-1][j]|g[i+1][j])*(g[i][j-1]|g[i][j+1])<1:c+=1;n=m;g[i][j]=0;[k:=t for t in r(4)if(v:=g[i+d[t]][j+d[t+1]])*(v-n)]
 for i in r(N)[::k>0 or-1]:
  for j in r(M)[::k<3 or-1]:
   if g[i][j]==n>g[a:=i+d[k]*c][b:=j+d[k+1]*c]:g[a][b]=n;g[i][j]=0
 return g
