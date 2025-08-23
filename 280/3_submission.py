def p(g):
 n=len(g)
 for y,x in[divmod(i,n)for i in range(n*n)if g[i//n][i%n]==2]:
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   if g[y+a][x+b]<1:break
  Y=y-a;X=x-b;k=0
  while n>Y>-1<X<n>2<g[Y][X]:k+=1;Y-=a;X-=b
  while n>y>-1<x<n:
   for t in range(-k,k+1):g[y+b*t][x+a*t]=3
   g[y][x]=2;y+=a;x+=b
 return g
