def p(g):
 for s in-1,1:
  x,y=divmod(sum(g,[]).index(8),13);t=0
  while-1<(x:=x-s*(t&2<1))<13>(y:=y+s*(t&2>0))>-1:g[x][y]=5;t+=1
 return g
