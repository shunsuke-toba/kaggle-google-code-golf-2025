def p(g):
 r=range;A=[(d,e)for k in r(100)if g[(d:=k//10)][(e:=k%10)]%5];t,l,a,b=A[0]+A[-1];a-=t-1;b-=l-1
 for k in r(100):
  if g[d:=k//10][e:=k%10]==5:
   for i in r(a):g[d+i][e:e+b]=g[t+i][l:l+b]
 return g
