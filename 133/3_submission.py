def p(g):
 r=range;l=len;h=l(g);w=l(g[0])
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
   if h>Y>=0<=X<w and g[Y][X]:c+=f(Y,X)
  return c
 C=[f(i//w,i%w)for i in r(h*w)if g[i//w][i%w]]
 B=min((c for c in C if c[2:]),key=l);d=[*zip(*B)][2];Y,X=B[d.index(p:=min(d,key=d.count))][:2]
 for c in C:
  m=int(l(A:=[v[:2]for v in c if v[2]==p])**.5);a,b=min(A);L=sum({v[2]for v in c})-p
  for y,x,t in B:
   o=b+(x-X)*m
   for i in r(m):g[a+(y-Y)*m+i][o:o+m]=[[p,L][t!=p]]*m
 return g
