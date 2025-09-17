def p(g):
 n=len(g);(a,b),(c,d)=[(y,x)for y in range(n)for x in range(n)if g[y][x]&1]
 def f(y,x,a,b,t=2):
  if n>(Y:=y+a)>-1<(X:=x+b)<n:
   v=g[Y][X]
   if v==2:return 1
   if t*v>7:return f(y,x,b,-a,t-1)or f(y,x,-b,a,t-1)
   if v-8 and f(Y,X,a,b,t):g[Y][X]=3;return 1
 g[2*a-c][2*b-d]-8 and f(a,b,a-c,b-d)or f(c,d,c-a,d-b)
 return g