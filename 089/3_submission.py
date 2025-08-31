R=range(-2,3)
def p(g):
 for k in 2,3:
  if(a:=[(i//13,i%13)for i in range(169)if sum(g,[])[i]==k]):_,T,B=max((len(t:=sorted((v,x,y)for x in R for y in R if-1<i+x<13>j+y>=0<(v:=g[i+x][j+y])!=k)),(i,j),t)for i,j in a);c=B[_>>1][0]
  for i,j in a:
   for v,x,y in B:
    if v==c:g[i+x][j+y*((i,j)==T or k*2-5)]=c
 return g