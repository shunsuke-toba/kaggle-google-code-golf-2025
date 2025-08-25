def p(g):
 for t,k in(8,3),(9,2):
  for n in range(t*t):
   i=n//t;j=n%t
   if all(all(R[j:j+k])for R in g[i:i+k]):
    h=k/2-.5;i+=h;j+=h
    for n in range(100):
     if v:=g[y:=n//10][x:=n%10]:
      y-=i;x-=j
      for _ in 0,0,0:x,y=-y,x;g[int(i+y)][int(j+x)]=v
    return g
