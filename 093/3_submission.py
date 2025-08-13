def p(g):
 H,W=len(g),len(g[0]);G=[(r,j)for r in range(H)for j in range(W)if g[r][j]==5];R=[[0]*W for _ in[0]*H]
 if G:
  a=min(r for r,j in G);b=max(r for r,j in G);c=min(j for r,j in G);d=max(j for r,j in G)
  for r in range(a,b+1):
   for j in range(c,d+1):R[r][j]=5
  for j in range(c,d+1):
   n=sum(0<g[r][j]!=5 for r in range(a))
   for i in range(n):R[a+~i][j]=5
   n=sum(0<g[r][j]!=5 for r in range(b+1,H))
   for i in range(n):R[b-~i][j]=5
  for r in range(a,b+1):
   n=sum(0<g[r][j]!=5 for j in range(c))
   for i in range(n):R[r][c+~i]=5
   n=sum(0<g[r][j]!=5 for j in range(d+1,W))
   for i in range(n):R[r][d-~i]=5
 return R
