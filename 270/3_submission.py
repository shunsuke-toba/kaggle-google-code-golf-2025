def p(g):
 r=[[0]*15 for _ in g]
 for t in 7,3:
  y,x=divmod(sum(g,[]).index(7//t),15);r[y][x]=7//t
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   a,b=y+Y,x+X
   while-1<a<15>b>-1:
    if g[a][b]==t:r[y+Y][x+X]=t;break
    a+=Y;b+=X
 return r
