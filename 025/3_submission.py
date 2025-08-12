def p(g):
 h,w=len(g),len(g[0]);o=[r[:]for r in g]
 for v in range(1,10):
  l=[sum(g[i][j]==v for i in range(h))for j in range(w)];c=[sum(g[i][j]==v for j in range(w))for i in range(h)]
  for y in range(h):
   for x in range(w):
    if g[y][x]==v and c[y]<w and l[x]<h:
     o[y][x]=0
     for d,e in(0,1),(1,0),(0,-1),(-1,0):
      a,b=y,x
      while-1<a+d<h and-1<b+e<w:a+=d;b+=e;o[a][b]==v and(c[a]==w or l[b]==h)and exec('o[a-d][b-e]=v')
 return o