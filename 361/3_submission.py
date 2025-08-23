def p(g,R=range):
 s=len(g)
 for k in 3,2:
  t=s-k+1
  for n in R(t*t):
   i,j=divmod(n,t)
   if all(all(r[j:j+k])for r in g[i:i+k]):
    r=k/2-.5;i+=r;j+=r
    for n in R(s*s):
     y,x=n//s,n%s;a,b=y-i,x-j
     if v:=g[y][x]:
      for m,n in(i-b,j+a),(i-a,j-b),(i+b,j-a):g[int(m)][int(n)]=v
    return g
