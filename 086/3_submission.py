def p(g):
 n=len(g);z=[*map(list,g)]
 for t in range(n*n):
  y,x=divmod(t,n)
  if g[y][x] and g[y-1][x]==g[y][x-1]==0:
   b=g[y][x];s=1
   while g[y][x+s]==b:s+=1
   a=g[y+1][x+1];B=y+s-1;E=x+s-1
   for i in range(y-s+2,B+s-1):
    for j in range(x-s+2,E+s-1):
     if y<=i<=B or x<=j<=E:
      z[i][j]=[b,a][y<=i<=B and x<=j<=E and (i in(y,B) or j in(x,E))]
 return z
