def p(g):
 l=len;r=range;w=l(g[0])
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
   if l(g)>Y>=0<=X<w and g[Y][X]:c+=f(Y,X)
  return c
 C=[f(i//w,i%w)for i in r(l(g)*w)if g[i//w][i%w]]
 B=min((c for c in C if l(c)>2),key=l)
 d=[*zip(*B)][2];Py,Px=B[d.index(p:=min(d,key=d.count))][:2]
 for c in C:
  m=int(l(A:=[(y,x)for y,x,v in c if v==p])**.5);a,b=min(A);L=sum({v for *_,v in c})-p
  for y,x,t in B:
   for i in r(m):g[a+(y-Py)*m+i][b+(x-Px)*m:b+(x-Px)*m+m]=[[p,L][t!=p]]*m
 return g

