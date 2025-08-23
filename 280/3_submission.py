def p(g):
 n=len(g)
 for y,x in[(i//n,i%n)for i in range(n*n)if g[i//n][i%n]==2]:
  a=(g[y-1][x]>2)-(g[y+1][x]>2);b=(g[y][x-1]>2)-(g[y][x+1]>2);k=1
  while n>y-a*k>-1<x-b*k<n and g[y-a*k][x-b*k]>2:k+=1
  while n>y>-1<x<n:
   for t in range(1-k,k):g[y+b*t][x+a*t]=3
   g[y][x]=2;y+=a;x+=b
 return g
