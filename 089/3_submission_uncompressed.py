def p(g):
 for k in range(2,4):
  a=[(x,y)for x in range(13) for y in range(13) if g[x][y]==k]
  for i,j in a:
   if(b:=sorted((v,x,y)for x in range(-2,3) for y in range(-2,3) if 0<=i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k))[2:]:p,q=i,j;c=b[len(b)//2][0];break
  for i,j in a:
   for v,x,y in b:
    if v==c:g[i+x][j+y*(i^p|j^q<1or k*2-5)]=c
 return g