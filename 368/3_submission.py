def p(g):
 R=range(10);A=[(i,j)for i in R for j in R if g[i][j]%5];t,l,a,b=A[0]+A[-1]
 for i in R:
  for j in R:
   for k in[*R[t:a+1]]*(g[i][j]==5):g[i+k-t][j:j+b-l+1]=g[k][l:b+1]
 return g