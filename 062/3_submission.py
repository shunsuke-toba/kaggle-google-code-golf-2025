def p(g):
 f=sum(g,[]);k=sum({*f})-2;x,y=divmod(f.index(2),10)
 b=k in g[x];a=(x,y)[b]+(g[x-1+b][y-b]!=k);g=[[3]*10 for _ in g];n=100
 while n:=n-1:
  i,j=divmod(n,10)
  if f[n]==k:g[i][j]=g[(2*a+~i,i)[b]][(j,2*a+~j)[b]]=k
 return g
