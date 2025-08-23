def p(g):
 l=len;h=l(g);w=l(g[0]);r=range
 def f(y,x):
  c=[(y,x,g[y][x])];g[y][x]=0
  for U,V in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
   if h>U>=0<=V<w and g[U][V]:c+=f(U,V)
  return c
 C=[f(i//w,i%w)for i in r(h*w)if g[i//w][i%w]]
 B=min((c for c in C if c[2:]),key=l)
 d=[*zip(*B)][2];Y,X=B[d.index(p:=min(d,key=d.count))][:2]
 for c in C:
  m=int(l(A:=[x[:2]for x in c if x[2]==p])**.5);a,b=min(A);L=sum({x[2]for x in c})-p
  for y,x,t in B:
   for i in r(m):g[a+(y-Y)*m+i][b+(x-X)*m:b+(x-X)*m+m]=[[p,L][t!=p]]*m
 return g
