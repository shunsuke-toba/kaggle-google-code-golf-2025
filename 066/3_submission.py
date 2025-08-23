def p(g):
 h=len(g);w=len(g[0]);(a,b),(c,d)=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==3]
 def f(y,x,A,B,t=0):
  y+=A;x+=B
  if not(-1<y<h and-1<x<w):return
  v=g[y][x]
  if v==2:return 1
  if v==8:return t<2 and (f(y-A,x-B,-B,A,t+1)or f(y-A,x-B,B,-A,t+1))
  if f(y,x,A,B,t):g[y][x]=3;return 1
 for y,x,A,B in(((a,b,0,-1),(c,d,0,1)),((a,b,-1,0),(c,d,1,0)))[a!=c]:
  if g[y+A][x+B]!=8 and f(y,x,A,B):break
 return g
