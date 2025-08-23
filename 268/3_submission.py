def p(g):
 n=len(g);R=range;r=lambda z:[*map(list,zip(*z[::-1]))]
 for k in R(4):
  x,y=zip(*((i,j)for i in R(n)for j in R(n)if g[i][j]))
  a,b=min(x),max(x);c,d=min(y),max(y)
  if 0 in g[a][c+1:d]:break
  g=r(g)
 for e in g[a+1:b]:e[c+1:d]=[4]*(d-c-1)
 for e in g[:b]:e[c+2:d-1]=[4]*(d-c-3)
 for j in R(a):
  if j<c+2:g[a-1-j][c+1-j]=4
  if j<=n-d:g[a-1-j][d-1+j]=4
 while k%4:g=r(g);k+=1
 return g
