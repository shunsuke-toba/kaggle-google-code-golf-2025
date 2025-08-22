def p(g,R=range):
 s=len(g)
 for k in 3,2:
  for i in R(s-k+1):
   for j in R(s-k+1):
    if all(g[y][x]for y in R(i,i+k)for x in R(j,j+k)):
     c,d=i+k/2-.5,j+k/2-.5
     for z in R(s*s):
      y,x=z//s,z%s;a,b=y-c,x-d;v=g[y][x]
      if v:
       for m,n in(c-b,d+a),(c-a,d-b),(c+b,d-a):
        g[int(m)][int(n)]=v
     return g
