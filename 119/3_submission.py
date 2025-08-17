def p(g):
 h=len(g);w=len(g[0])
 r=[a.count(2)for a in g];c=[b.count(2)for b in zip(*g)]
 s=[[y,x,-i,-j]for y in range(h)for x in range(w)if g[y][x]==8 for i,j in((1,1),(1,-1),(-1,1),(-1,-1))if 0<=y+i<h and 0<=x+j<w and g[y+i][x+j]==8]
 for y,x,i,j in s:
  while 1:
   Y,X=y+i,x+j
   if not(0<=Y<h and 0<=X<w):break
   if g[Y][X]==2:
    if c[X]>r[Y]:j=-j
    else:i=-i
   else:
    y,x=Y,X
    if g[y][x]<1:g[y][x]=3
 return g
