def p(g,r=range):
 s=len(g)
 for k in 3,2:
  t=s-k+1
  for n in r(t*t):
   i,j=divmod(n,t)
   if all(min(R[j:j+k])for R in g[i:i+k]):
    h=k/2-.5;i+=h;j+=h
    for n in r(s*s):
     if v:=g[y:=n//s][x:=n%s]:
      a,b=y-i,x-j
      for _ in 0,0,0:a,b=-b,a;g[int(i+a)][int(j+b)]=v
    return g
