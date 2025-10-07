def p(g):
 n=len(g);(a,b),(c,d)=[(y,x)for y in range(n)for x in range(n)if g[y][x]&1]
 def f(a,b,c,d,t,u=0):
  if n>(y:=a+c)>-1<(x:=b+d)<n:
   if g[y][x]==2:return g[y][x]
   if g[y][x]^8 and f(y,x,c,d,t,1):g[y][x]=3;return g[y][x]
   if u and g[y][x]*t>7:return f(a,b,d,-c,t-1,u)or f(a,b,-d,c,t-1,u)
 f(a,b,a-c,b-d,2)or f(c,d,c-a,d-b,2)
 return g