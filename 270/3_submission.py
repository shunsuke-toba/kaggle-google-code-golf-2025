def p(g):
 r=[[0]*15 for _ in g]
 for i in 1,2:
  y,x=divmod(sum(g,[]).index(i),15);r[y][x]=i;t=11-4*i
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   c,d=a,b=y+Y,x+X
   while-1<a<15>b>-1:
    if g[a][b]==t:r[c][d]=t;break
    a+=Y;b+=X
 return r
