def p(g):
 for y,x,b,a,n in[(y,x,b,g[y+1][x+1],2-(g[y+3][x]<1))for y,r in enumerate(g)for x,b in enumerate(r)if b>g[y-1][x]+r[x-1]<1]:
  for i in range(-n,n+n+2):
   for j in range(n+2):g[y+i][x+j]=b
  for i in range(n+2):
   for j in range(-n,n+n+2):g[y+i][x+j]=b
  for i in range(n+2):
   for j in range(n+2):g[y+i][x+j]=a
  for i in range(1,n+1):
   for j in range(1,n+1):g[y+i][x+j]=b
 return g