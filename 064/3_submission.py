def p(g):
 h=len(g);w=len(g[0]);r=[*map(list,g)];s=sum(g,[]);b=max(s,key=s.count);v=set();M=0;R=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]-b and(i,j)not in v:
    o=g[i][j];A=i;D=j
    while D+1<w and g[i][D+1]==o:D+=1
    while A+1<h and g[A+1][j:D+1]==[o]*(D-j+1):A+=1
    if(k:=(D-j+1)*(A-i+1))-1:
     v|={(x,y)for x in range(i,A+1)for y in range(j,D+1)}
     if k>M:M=k;R=[(i,j,A,D)]
     elif k==M:R+=[(i,j,A,D)]
 for a,d,A,D in R:
  for s in 0,1,2,3:
   for m in range(*[(d,D+1),(a,A+1)][s>1]):
    i,j,p,q=o=[(a-1,m,-1,0),(A+1,m,1,0),(m,d-1,0,-1),(m,D+1,0,1)][s];L=u=v=0
    while-1<i<h and-1<j<w:
     if g[i][j]-b:L=g[i][j];u=i;v=j
     i+=p;j+=q
    i,j,p,q=o
    while L and(i,j)!=(u,v):
     if g[i][j]==b:r[i][j]=L
     i+=p;j+=q
 return r
