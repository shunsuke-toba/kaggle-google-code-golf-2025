def p(g):
 n=len(g);R=range;r=lambda z:[*map(list,zip(*z[::-1]))]
 for k in R(4):
  s=[(i,j)for i in R(n)for j in R(n)if g[i][j]];a,c=s[0];b,d=s[-1]
  if 0 in g[a][c:d]:break
  g=r(g)
 y=d-c-1
 for i in R(b):t=i>a;g[i][c+2-t:d+t-1]=[4]*(y-2+2*t)
 for j in R(a):
  h=g[a+~j]
  if j<c+2:h[c+1-j]=4
  if j<=n-d:h[d-1+j]=4
 for _ in R(4-k):g=r(g)
 return g
