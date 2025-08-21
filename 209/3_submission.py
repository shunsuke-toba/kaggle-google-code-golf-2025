def p(g):
 y=len(g);x=len(g[0]);a=y;c=x;b=d=0
 for t in range(y*x):
  r=t//x;j=t%x
  if g[r][j]==4:a=min(a,r);b=max(b,r);c=min(c,j);d=max(d,j)
 e=y;i=x;f=j=0
 for t in range(y*x):
  r=t//x;o=t%x
  if g[r][o]and not(a<=r<=b and c<=o<=d):e=min(e,r);f=max(f,r);i=min(i,o);j=max(j,o)
 h=f-e+1;w=j-i+1;z=k=P=0
 for s in(2,3,4):
  H=h*s;W=w*s
  for r in range(a,b-H+2):
   for o in range(c,d-W+2):
    m=n=0
    for t in range(H*W):
      if(v:=g[r+t//W][o+t%W]):n+=1;m+=v!=g[e+t//W//s][i+t%W//s]
    if m<1<n-z+1:z=n;k=s;P=r,o
 r,o=P
 for q in range(h*k):g[r+q][o:o+w*k]=[g[e+q//k][i+p//k]for p in range(w*k)]
 return[r[c:d+1]for r in g[a:b+1]]
