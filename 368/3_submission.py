def p(g):
 a,b=zip(*[divmod(k,10)for k in range(100)if g[k//10][k%10]%5]);t=min(a);l=min(b);h=max(a)-t+1;w=max(b)-l+1
 for Y in range(11-h):
  for X in range(11-w):
   if{g[Y+i][X+j]for i in range(h)for j in range(w)}=={5}:
    for i in range(h):g[Y+i][X:X+w]=g[t+i][l:l+w]
 return g
