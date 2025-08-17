def p(g):
 i,j=divmod(sum(g,[]).index(8),13)
 def w(s):
  x,y=i,j
  while 1:
   for dx,dy in(-s,0),(0,s):
    for _ in 0,1:
     if 13>(x:=x+dx)>-1<(y:=y+dy)<13:g[x][y]=5
     else:return
 w(1);w(-1)
 return g