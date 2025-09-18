t=range(13);r=range(-2,3)
def p(g):
 for k in 2,3:
  a=[(x,y)for x in t for y in t if g[x][y]==k]
  for i,j in a:
   if len(b:=sorted((v,x,y)for x in r for y in r if-1<i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k))>2:p,q=i,j;c=b[len(b)//2][0];break
  for i,j in a:
   for v,x,y in b:
    if v==c:g[i+x][j+y*(i^p|j^q<1or k*2-5)]=c
 return g