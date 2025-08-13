def p(g):
 h,w=len(g),len(g[0]);r=[x[:]for x in g];c={}
 for x in g:
  for y in x:c[y]=c.get(y,0)+1
 b=max(c,key=c.get);v=set();R=[]
 for i in range(h):
  for j in range(w):
   if(i,j)not in v and g[i][j]-b:
    o=g[i][j];a=A=i;d=D=j
    while D<w-1 and g[i][D+1]==o:D+=1
    while A<h-1 and all(g[A+1][x]==o for x in range(d,D+1)):A+=1
    if all(g[x][y]==o for x in range(a,A+1)for y in range(d,D+1))and(a-A or d-D):v|={(x,y)for x in range(a,A+1)for y in range(d,D+1)};R+=[(A-a+1)*(D-d+1),a,d,A,D],
 if R:M=max(R)[0];R=[x for x in R if x[0]==M]
 for _,a,d,A,D in R:
  for s in 0,1,2,3:
   for m in range(*[(d,D+1),(a,A+1)][s>1]):
    E=[];L=C=0;i,j,p,q=[(a-1,m,-1,0),(A+1,m,1,0),(m,d-1,0,-1),(m,D+1,0,1)][s]
    while(s<2 and-1<i<h)or(s>1 and-1<j<w):E+=(i,j),;L,C=(g[i][j],i if s<2 else j)if g[i][j]-b else(L,C);i+=p;j+=q
    for x,y in E:
     if L and((x if s<2 else y)>C if s%2<1 else(x if s<2 else y)<C)and g[x][y]==b:r[x][y]=L
 return r
