def p(g):
 n=len(g)-1;m=n-1
 for y in range(m*m):
  x=y%m+1;y=y//m+1
  if(c:=g[y][x])and(d:=(g[y+1][x]-g[y-1][x])//c)and(e:=(g[y][x+1]-g[y][x-1])//c)and g[y+d][x+e]^c:
   c=g[y+2*d][x+2*e]
   while 0<y<n>0<x<n:g[y:=y-d][x:=x-e]=c
 return g
