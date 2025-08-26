R=range(-2,3)
def p(g):
 for k in 2,3:
  if(a:=[(i//13,i%13)for i,v in enumerate(sum(g,[]))if v==k]):_,i,j,B=max((len(t:=[(v,x,y)for x in R for y in R if-1<i+x<13>j+y>=0<k!=(v:=g[i+x][j+y])>0]),i,j,t)for i,j in a);a.remove((i,j));c=sorted(B)[len(B)>>1][0]
  for i,j in a:
   for v,x,y in B:
    if v==c:g[i+x][j+y*(k*2-5)]=c
 return g
