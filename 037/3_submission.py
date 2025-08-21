def p(g):
 d={}
 for k in range(100):
  if v:=g[y:=k//10][x:=k%10]:
   try:
    a,b=d[v];n=y-a
    while n+1:g[a+n][b+n*(1-2*(x<b))]=v;n-=1
   except:d[v]=y,x
 return g
