def p(g):
 n=len(g);(a,b),(c,d)=[(y,x)for y in range(n)for x in range(n)if g[y][x]&1]
 def f(y,x,a,b,t):
  if n>(w:=y+a)>-1<(v:=x+b)<n:
   if g[w][v]==2:return g[w][v]
   if t*g[w][v]>7:return f(y,x,b,-a,t-1)or f(y,x,-b,a,t-1)
   if g[w][v]-8 and f(w,v,a,b,t):g[w][v]=3;return g[w][v]
 g[2*a-c][2*b-d]-8 and f(a,b,a-c,b-d,2)or f(c,d,c-a,d-b,2)
 return g