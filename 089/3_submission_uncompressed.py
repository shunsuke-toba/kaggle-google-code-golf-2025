def p(g):
 for k in 2,3:
  a=[(x,y)for x in range(13)for y in range(13)if g[x][y]==k]
  for i,j in a:
   if(b:=sorted((v,x,y)for x in range(-2,3)for y in range(-2,3)if 0<=i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k))[2:]:s=i,j;c=b[len(b)//2][0];break
  for i,j in a:
   for v,x,y in b:
    if v==c:g[i+x][j+y*((i,j)==s or k-2 or-1)]=c
 return g