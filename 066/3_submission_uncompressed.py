def p(g):
 n=len(g);(a,b),(c,d)=[(y,x)for y in range(n)for x in range(n)if g[y][x]&1]
 def f(a,b,c,d,t):
  if n>(y:=a+c)>-1<(x:=b+d)<n:
   if g[y][x]==2:return g[y][x]
   if t*g[y][x]>7:return f(a,b,d,-c,t-1)or f(a,b,-d,c,t-1)
   if g[y][x]-8 and f(y,x,c,d,t):g[y][x]=3;return g[y][x]
 g[2*a-c][2*b-d]-8 and f(a,b,a-c,b-d,2)or f(c,d,c-a,d-b,2)
 return g