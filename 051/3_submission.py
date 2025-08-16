def p(g):
 for y in range(1,len(g)-1):
  r=g[y]
  for x in range(1,len(r)-1):
   c=r[x]
   a,b=g[y-1][x],g[y+1][x]
   if a!=c!=b and a*b<1<=a+b:
    a=1-2*(a>0);k=y
    while 0<=(k:=k+a)<len(g):g[k][x]=g[k][x]or c
   a,b=r[x-1],r[x+1]
   if a!=c!=b and a*b<1<=a+b:
    a=1-2*(a>0);k=x
    while 0<=(k:=k+a)<len(r):r[k]=r[k]or c
 return g
