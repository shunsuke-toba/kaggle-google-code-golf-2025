def p(g):
 H,W=len(g),len(g[0]);r=[x[:]for x in g];v=set()
 def d(i,j):
  if(i,j)not in v and-1<i<H and-1<j<W and g[i][j]==1:v.add((i,j));return[(i,j)]+d(i-1,j)+d(i+1,j)+d(i,j-1)+d(i,j+1)
  return[]
 for k in range(H*W):
  x,y=k//W,k%W
  if g[x][y]==1 and(x,y)not in v:
   c=d(x,y)
   if c:
    *C,=zip(*c);a=min(C[0]);b=max(C[0]);e=min(C[1]);f=max(C[1]);F=0
    for m in range((b-a+1)*(f-e+1)):
     i,j=divmod(m,f-e+1);i+=a;j+=e
     if g[i][j]>1:F=g[i][j];break
    if F:
     a and[exec("r[a-1][j]=F")for j in range(e,f+1)]
     [g[i][j]!=1 and exec("r[i][j]=F")for i in range(a,b+1)for j in range(e,f+1)]
 return r
