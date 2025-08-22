def p(g):
 f=sum(g,[]);k=(set(f)-{0,2}).pop();x,y=divmod(f.index(2),10)
 b=k in g[x][y-1:y+2];a=(x,y)[b]+(g[x-1+b][y-b]!=k)
 o=[[3]*10 for _ in g]
 for n in range(100):
  i,j=divmod(n,10)
  if g[i][j]==k:o[i][j]=o[b and i or 2*a+~i][b and 2*a+~j or j]=k
 return o
