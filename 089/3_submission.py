R=range(-2,3)
def p(g):
 for k in 2,3:
  a=[(i//13,i%13)for i,v in enumerate(sum(g,[]))if v==k];B=s=()
  for i,j in a:
   t=[(v,x,y)for x in R for y in R if -1<i+x<13>j+y>=0<k!=(v:=g[i+x][j+y])>0]
   if(l:=len(t))>len(B):c=sorted(t)[l//2][0];B=[(x,y)for v,x,y in t if v==c];s=i,j
  for i,j in a:
   if(i,j)!=s:
    for x,y in B:g[i+x][j+y*(k*2-5)]=c
 return g
