def p(G,E=enumerate):
 R=[];a=b=c=d=99;e=f=g=h=0;m=min;M=max
 for i,r in E(G):
  for j,v in E(r):
   if v==2:R+=[(i,j)];a=m(a,i);e=M(e,i);b=m(b,j);f=M(f,j)
   elif v==8:c=m(c,i);g=M(g,i);d=m(d,j);h=M(h,j)
 y=x=0
 if e<c:y=c-e-1
 elif g<a:y=g-a+1
 else:x=d-f-1 if f<d else h-b+1
 for i,j in R:G[i][j]=0
 for i,j in R:G[i+y][j+x]=2
 return G
