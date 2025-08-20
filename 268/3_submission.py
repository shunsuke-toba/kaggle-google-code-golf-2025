def p(g):
 h=len(g)
 c=t=h;l=99;b=r=0
 for y,R in enumerate(g):
  for x,v in enumerate(R):
   if v:c=v;t=min(t,y);b=max(b,y);l=min(l,x);r=max(r,x)
 for y in range(t+1,b):g[y][l+1:r]=[4]*(r-l-1)
 def f(y,x,dy,dx):
  y+=dy;x+=dx
  while-1<y<h and-1<x<len(g[0])and g[y][x]<1:g[y][x]=4;y+=dy;x+=dx
 for y,dy in (t,-1),(b,1):
  for x in range(l,r+1):
   if g[y][x]^c:g[y][x]=4;f(y,x,dy,0);(x<=l or g[y][x-1]==c)and f(y,x,dy,-1);(x>=r or g[y][x+1]==c)and f(y,x,dy,1)
 for x,dx in (l,-1),(r,1):
  for y in range(t,b+1):
   if g[y][x]^c:g[y][x]=4;f(y,x,0,dx);(y<=t or g[y-1][x]==c)and f(y,x,-1,dx);(y>=b or g[y+1][x]==c)and f(y,x,1,dx)
 return g
