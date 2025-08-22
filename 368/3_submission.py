def p(g):
 r=range;a,b=zip(*[divmod(k,10)for k in r(100)if g[k//10][k%10]%5]);t=min(a);l=min(b);a=max(a)-t+1;b=max(b)-l+1
 for Y in r(11-a):
  for X in r(11-b):
   if{g[Y+i][X+j]for i in r(a)for j in r(b)}=={5}:
    for i in r(a):g[Y+i][X:X+b]=g[t+i][l:l+b]
 return g
