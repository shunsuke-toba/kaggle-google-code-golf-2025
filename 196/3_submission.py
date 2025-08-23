def p(g):
 n=len(g)
 def f(i,j):
  if-1<i<n>j>=0==g[i][j]-1:g[i][j]=0;return[(i,j)]+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)
  return[]
 for k in range(n*n):
  if c:=f(k//n,k%n):
   h,w=[max(t)-min(t)for t in zip(*c)]
   for y,x in c:g[y][x]=1+2*(len(c)/2==h+w)*(h>1<w)
 return g
