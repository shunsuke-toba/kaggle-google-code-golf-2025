def p(g):
 R=range(10);A=[(i,j)for i in R for j in R if g[i][j]%5];t,l,a,b=A[0]+A[-1];a-=t-1;b-=l-1
 for i in R:
  for j in R:
   if g[i][j]==5:
    for k in R[:a]:g[i+k][j:j+b]=g[t+k][l:l+b]
 return g
