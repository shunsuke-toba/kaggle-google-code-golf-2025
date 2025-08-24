def p(g):
 s=len(g)
 for k in 3,2:
  t=s-k+1
  for n in range(t*t):
   i=n//t;j=n%t
   if min(min(R[j:j+k])for R in g[i:i+k]):
    h=k/2-.5;i+=h;j+=h
    for n in range(s*s):
     if v:=g[y:=n//s][x:=n%s]:
      y-=i;x-=j
      for _ in 0,0,0:x,y=-y,x;g[int(i+y)][int(j+x)]=v
    return g
