def p(g,b=324):
 while b:
  b-=1;e=(b&2)-1;d=b%2*2-1;x=b//4%9;k=b//36+(e>0);v=g[x-d];v=g[x][k-e]&v[k-e]&v[k]
  while 0<x<9>k>0:g[x:=x+d][k:=k+e]+=v
 return g