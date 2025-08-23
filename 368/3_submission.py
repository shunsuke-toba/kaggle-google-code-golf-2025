def p(g):
 r=range;a,b=zip(*[divmod(k,10)for k in r(100)if g[k//10][k%10]%5]);t=min(a);l=min(b);a=max(a)-t+1;b=max(b)-l+1
 for Y in r(10):
  for X in r(10):
   if g[Y][X]==5:
    for i in r(a):g[Y+i][X:X+b]=g[t+i][l:l+b]
 return g
