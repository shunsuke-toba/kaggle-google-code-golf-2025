def p(g):
 r=range;A=[divmod(k,10)for k in r(100)if g[k//10][k%10]%5];(t,l),(a,b)=min(A),max(A);a-=t-1;b-=l-1
 for k in r(100):
  if g[k//10][k%10]==5:
   for i in r(a):g[k//10+i][k%10:k%10+b]=g[t+i][l:l+b]
 return g
