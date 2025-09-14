r=range(-2,3)
def p(g):
 for k in 2,3:
  a=[(i//13,i%13)for i in range(169)if sum(g,[])[i]==k]
  for i,j in a:
   if(b:=sorted((v,x,y)for x in r for y in r if-1<i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k))[2:]:c=b[len(b)>>1][0];p,q=i,j;break
  for i,j in a:
   for v,x,y in b:
    if v==c:g[i+x][j+y*(i^p|j^q<1or k*2-5)]=c
 return g