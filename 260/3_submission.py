def p(g):
 c,k=next((v,y-x)for y,r in enumerate(g)for x,v in enumerate(r)if v%5);a=b=0
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==5:
    g[y][x]=0;d=y-x-k;b<d and(b:=d);a<-d and(a:=-d)
 for s,d in(-1,a),(1,b):
  for y in range(len(g)):
   if d>0 and 0<=(x:=y-k-s*(d+2))<len(g[0]):g[y][x]=c
 return g
