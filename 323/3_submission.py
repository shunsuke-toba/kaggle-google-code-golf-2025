def p(g):
 i=sum(g,[]).index(8)
 for s in-1,1:
  x,y=i//13,i%13;t=0
  while 13>(x:=x-s*(t&2<1))>-1<(y:=y+s*(t&2>0))<13:g[x][y]=5;t+=1
 return g
