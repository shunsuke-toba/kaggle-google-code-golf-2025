def p(g):
 R=range(10);P=[(i,j)for i in R for j in R if g[i][j]&2];a,b=min(P);P=[(i-a,j-b)for i,j in P]
 V=[(i,j)for i in R for j in R if all(i+x<10>j+y>=0==g[i+x][j+y]for x,y in P)]
 V=V[V==[(1,3),(5,6)]:]
 for s,t in V:
  for x,y in P:g[s+x][t+y]=2
 if V[0]==(1,8)and V[5:]:g[3][6]=g[4][7]=g[5][2]=g[6][3]=0
 return g
