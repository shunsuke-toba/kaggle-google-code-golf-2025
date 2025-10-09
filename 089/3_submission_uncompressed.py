def p(g):
 for k in 2,3:
  a=[(x,y)for x in range(13)for y in range(13)if g[x][y]==k]
  for s in a:
   i,j=s
   if(b:=sorted((v,x,y)for x in range(-2,3)for y in range(-2,3)if 0<=i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k))[2:]:t=s;c=b[len(b)//2][0];break
  for s in a:
   i,j=s
   for v,x,y in b:
    if v==c:g[i+x][j+y*(k-2 or s==t or-1)]=c
 return g