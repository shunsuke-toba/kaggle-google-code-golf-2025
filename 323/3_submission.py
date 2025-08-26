def p(g):
 for s in-1,1:
  x,y=divmod(sum(g,[]).index(8),13);t=0
  while-1<(x:=x-s*(t<2))<13>(y:=y+s*(t>1))>-1:g[x][y]=5;t=t+1&3
 return g
