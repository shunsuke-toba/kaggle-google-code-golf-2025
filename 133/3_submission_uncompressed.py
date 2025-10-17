def p(n):
 i=len(n);w=len(n[0])
 def f(y,x):
  a=[(y,x,n[y][x])];n[y][x]=0
  for y,x in(y+1,x),(y,x+1),(y-1,x),(y,x-1):
   if w>x>-1<y<i>n[y][x]>0:a+=f(y,x)
  return a
 s=[f(y,x)for y in range(i)for x in range(w)if n[y][x]]
 d=min((len(t)<3,len(t),t)for t in s)[2]
 u,c,o=min((sum(v==t[2]for y,x,v in d),t)for t in d)[1]
 for t in s:
  a=[(y,x)for y,x,v in t if v==o];m=int(len(a)**.5);q=min(v for y,x,v in t if v^o)
  for y,x,v in d:
   for s,r in a:n[(y-u)*m+s][(x-c)*m+r]=(q,o)[v==o]
 return n