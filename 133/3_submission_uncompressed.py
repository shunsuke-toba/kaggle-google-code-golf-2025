def p(g):
 l=len;h=l(g);w=l(g[0])
 def f(y,x):
  a=[(y,x,g[y][x])];g[y][x]=0
  for y,x in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
   if w>x>-1<y<h>g[y][x]>0:a+=f(y,x)
  return a
 C=[f(y,x)for y in range(h)for x in range(w)if g[y][x]]
 B=min(C,key=lambda t:(l(t)<3,l(t)))
 r,c,p=min(B,key=lambda t:sum(v==t[2]for y,x,v in B))
 for t in C:
  a=[(y,x)for y,x,v in t if v==p or(q:=v)*0];m=int(l(a)**.5)
  for y,x,v in B:
   for i,j in a:g[(y-r)*m+i][(x-c)*m+j]=(p,q)[v!=p]
 return g
