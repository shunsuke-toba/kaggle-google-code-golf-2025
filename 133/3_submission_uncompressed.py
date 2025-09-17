def p(g):
 h=len(g);w=len(g[0])
 def f(y,x):
  a=[(y,x,g[y][x])];g[y][x]=0
  for y,x in(y+1,x),(y,x+1),(y-1,x),(y,x-1):
   if w>x>-1<y<h>g[y][x]>0:a+=f(y,x)
  return a
 s=[f(y,x)for y in range(h)for x in range(w)if g[y][x]]
 b=min(s,key=lambda t:(len(t)<3,len(t)))
 r,c,p=min(b,key=lambda t:sum(v==t[2]for y,x,v in b))
 for t in s:
  a=[(y,x)for y,x,v in t if v==p or((q:=v)and[])];m=int(len(a)**.5)
  for y,x,v in b:
   for i,j in a:g[(y-r)*m+i][(x-c)*m+j]=(q,p)[v==p]
 return g