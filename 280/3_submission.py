def p(g):
 n=len(g)
 for y,x in[(i//n,i%n)for i in range(n*n)if g[i//n][i%n]==2]:
  a=(g[y-1][x]-g[y+1][x])//3;b=(g[y][x-1]-g[y][x+1])//3;k=1
  try:
   while g[y-a*k][x-b*k]>2:k+=1
  except:0
  while n>y>-1<x<n:
   for t in range(1-k,k):g[y+b*t][x+a*t]=2+(t!=0)
   y+=a;x+=b
 return g
