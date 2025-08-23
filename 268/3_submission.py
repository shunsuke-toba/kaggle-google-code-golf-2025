def p(g):
 n=len(g);R=range;r=lambda z:[*map(list,zip(*z[::-1]))]
 for k in R(4):
  x,y=zip(*[(i,j)for i in R(n)for j in R(n)if g[i][j]])
  a,b=min(x),max(x);c,d=min(y),max(y)
  if 0 in g[a][c+2:d-1]:break
  g=r(g)
 w=d-c-1
 for e in g[a+1:b]:e[c+1:d]=[4]*w
 for e in g[:b]:e[c+2:d-1]=[4]*(w-2)
 for j in R(a):
  i=a-1-j;L=c+1-j;E=d-1+j
  if L>=0:g[i][L]=4
  if E<n:g[i][E]=4
 for k in R(-k%4):g=r(g)
 return g
