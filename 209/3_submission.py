def p(g):
 a=e=y=len(g);c=i=x=len(g[0]);b=d=f=j=0;L=()
 for t in range(y*x):
  v=g[r:=t//x][o:=t%x]
  if v==4:a=min(a,r);b=max(b,r);c=min(c,o);d=max(d,o)
  elif v:L+=(r,o),
 for r,o in L:
  if r<a or r>b or o<c or o>d:e=min(e,r);f=max(f,r);i=min(i,o);j=max(j,o)
 h=f-e+1;w=j-i+1;z=k=R=O=0
 for s in 2,3,4:
  W=w*s
  for r in range(a,b-h*s+2):
   for o in range(c,d-W+2):
    m=n=0
    for t in range(h*s*W):
     if(v:=g[r+t//W][o+t%W]):n+=1;m+=v!=g[e+t//W//s][i+t%W//s]
    if m<1<n-z:z=n;k=s;R=r;O=o
 for q in range(h*k):g[R+q][O:O+w*k]=[g[e+q//k][i+p//k]for p in range(w*k)]
 return[r[c:d+1]for r in g[a:b+1]]
