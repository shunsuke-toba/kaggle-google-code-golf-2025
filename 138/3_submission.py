def p(g):
 h=len(g);w=len(g[0]);R=range(1,10)
 a=[i for i,c in enumerate(zip(*g))if max(map(c.count,R))>=h-2]
 b=[i for i,r in enumerate(g)if max(map(r.count,R))>=w-2]
 g=[r[a[0]:a[1]+1]for r in g[b[0]:b[1]+1]]
 h=len(g);w=len(g[0]);D={g[0][1]:(-1,0),g[-1][1]:(1,0),g[1][0]:(0,-1),g[1][-1]:(0,1)}
 for y in range(1,h-1):
  for x in range(1,w-1):
   d=D.get(c:=g[y][x])
   if d:
    i,j=y+d[0],x+d[1]
    while 0<=i<h and 0<=j<w:
     g[i][j]=c;i+=d[0];j+=d[1]
 return g
