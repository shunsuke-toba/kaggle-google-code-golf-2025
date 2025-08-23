def p(g):
 n=len(g)
 def f(i,j):
  if-1<i<n>j>=0<g[i][j]<2:g[i][j]=0;c.append((i,j));f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for k in range(n*n):
  c=[];f(k//n,k%n)
  if c:h,w=[max(t)-min(t)for t in zip(*c)]
  for y,x in c:g[y][x]=1+2*(c and len(c)/2==h+w>h>1<w)
 return g
