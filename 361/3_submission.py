def p(g,R=range):
 s=len(g)
 for k in 3,2:
  t=s-k+1
  for n in R(t*t):
   i,j=divmod(n,t)
   if all(min(r[j:j+k])for r in g[i:i+k]):
    r=k/2-.5;i+=r;j+=r
    for n in R(s*s):
     if v:=g[y:=n//s][x:=n%s]:
      a,b=y-i,x-j
      for m,n in(-b,a),(-a,-b),(b,-a):g[int(i+m)][int(j+n)]=v
    return g
