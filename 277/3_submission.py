def p(g):
 r=range;h=len(g);w=len(g[0]);C=[]
 for i in r(h):
  for j in r(w):
   if g[i][j]:
    c=[(i,j)];g[i][j]=0
    for x,y in c:
     for X in r(x-1,x+2):
      for Y in r(y-1,y+2):
       if-1<X<h and-1<Y<w and g[X][Y]:g[X][Y]=0;c+=[(X,Y)]
    C+=c,
 m=max(map(len,C))
 for c in C:
  for x,y in c:g[x][y]=1+(len(c)<m)
 return g
