def p(g):
 l=len;r=range;h=l(g);w=l(g[0])
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for Y,X in(1,0),(-1,0),(0,1),(0,-1):
   Y+=y;X+=x
   if h>Y>=0<=X<w and g[Y][X]:c+=f(Y,X)
  return c
 C=[f(y,x)for y in r(h)for x in r(w)if g[y][x]]
 B=min((c for c in C if l(c)>2),key=l)
 d=[*zip(*B)][2];p=min(d,key=d.count);a,b=B[d.index(p)][:2];B=[(y-a,x-b,v)for y,x,v in B]
 for c in C:
  A=[(y,x)for y,x,v in c if v==p];a,b=min(A);m=int(l(A)**.5);L=next(v for *_,v in c if v^p)
  for u,v,t in B:
   for i in r(m):g[a+u*m+i][b+v*m:b+v*m+m]=[(p,L)[t!=p]]*m
 return g
