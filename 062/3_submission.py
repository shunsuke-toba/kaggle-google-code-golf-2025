def p(g):
 s=10;f=sum(g,[]);k=sum({*f})-2;i=f.index(2);a=(i//s,i%s)[b:=k in g[i//s]]+(k>f[i-s+9*b]);g=[[3]*s for g in g];n=s*s
 while n:=n-1:
  if f[n]==k:g[i:=n//s][j:=n%s]=g[(2*a+~i,i)[b]][(j,2*a+~j)[b]]=k
 return g