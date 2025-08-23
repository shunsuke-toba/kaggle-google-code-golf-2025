def p(g):
 (a,b),(c,d)=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==3]
 def f(y,x,a,b,t=2):
  y+=a;x+=b
  if len(g)>y>=0<=x<len(g[0]):
   v=g[y][x]
   if v==2:return 1
   if v==8 and t and(f(y-a,x-b,b,-a,t-1)or f(y-a,x-b,-b,a,t-1)):return 1
   if v-8 and f(y,x,a,b,t):g[y][x]=3;return 1
 for y,x,a,b in(((a,b,0,-1),(c,d,0,1)),((a,b,-1,0),(c,d,1,0)))[a!=c]:
  if g[y+a][x+b]-8 and f(y,x,a,b):break
 return g