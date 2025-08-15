def p(g):
 h=len(g);w=len(g[0]);v=set()
 for i in range(h*w):
  y,x=divmod(i,w);c=g[y][x]
  if c-9 and i not in v:
   m=[i];v|={i};e=0
   for z in m:
    y,x=divmod(z,w)
    for n in(z-1,z+1,z-w,z+w):
     if 0<=n<h*w and-2<n%w-x<2 and g[n//w][n%w]==c:
      e+=1
      if n not in v:v|={n};m+=[n]
   if e>=2*len(m):
    for z in m:g[z//w][z%w]=8
 return g
