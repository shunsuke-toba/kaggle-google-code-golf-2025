def p(g,R=range):
 h,w=len(g),len(g[0])
 for k in 3,2:
  for i in R(h-k+1):
   for j in R(w-k+1):
    if all(g[y][x]for y in R(i,i+k)for x in R(j,j+k)):
     c,d=i+k/2-.5,j+k/2-.5
     for z in R(h*w):
      y,x=z//w,z%w;v=g[y][x];a,b=y-c,x-d
      for m,n in(c-b,d+a),(c-a,d-b),(c+b,d-a):
       if 0<v<h>m>-1<n<w:g[int(m)][int(n)]=v
     return g