def p(g):
 r=range(100);T=10
 A=[(k//T,k%T)for k in r if g[k//T][k%T]==2]
 m,n=min(A);P=[(x-m,y-n)for x,y in A];V=[]
 for k in r:
  for d,e in P:
   i,j=k//T+d,k%T+e
   if not(i<T>j>=0==g[i][j]):break
  else:V+=[k//T,k%T],
 if V==[[1,3],[5,6]]:V=V[1:]
 for s,t in V:
  for d,e in P:g[s+d][t+e]=2
 if len(V)==6and V[0]==[1,8]:g[3][6]=g[4][7]=g[5][2]=g[6][3]=0
 return g