def p(g):
 f=sum(g,[]);k=sum({*f})-2;i=f.index(2);a=(i//10,i%10)[b:=k in g[i//10]]+(k>f[i-10+9*b]);g=[[3]*10for g in g];n=100
 while n:=n-1:
  if f[n]==k:g[i:=n//10][j:=n%10]=g[(2*a+~i,i)[b]][(j,2*a+~j)[b]]=k
 return g