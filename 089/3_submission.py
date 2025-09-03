R=range(-2,3)
def p(g):
 for k in 2,3:
  a=[(i//13,i%13)for i in range(169)if sum(g,[])[i]==k]
  for i,j in a:
   if (B:=sorted((v,x,y)for x in R for y in R if-1<i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k))[2:]:c=B[len(B)>>1][0];break
  for I,J in a:
   for v,x,y in B:
    if v==c:g[I+x][J+y*((I,J)==(i,j)or k*2-5)]=c
 return g