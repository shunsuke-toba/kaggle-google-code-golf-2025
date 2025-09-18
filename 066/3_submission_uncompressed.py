def p(g):
 n=len(g);(a,b),(c,d)=[(y,x)for y in range(n)for x in range(n)if g[y][x]&1]
 def f(y,x,a,b,t=2):
  if n>(Y:=y+a)>-1<(X:=x+b)<n:
   if g[Y][X]==2:return g[Y][X]
   if t*g[Y][X]>7:return f(y,x,b,-a,t-1)or f(y,x,-b,a,t-1)
   if g[Y][X]-8 and f(Y,X,a,b,t):g[Y][X]=3;return g[Y][X]
 g[2*a-c][2*b-d]-8 and f(a,b,a-c,b-d)or f(c,d,c-a,d-b)
 return g