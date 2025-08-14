def p(g):
 H=len(g);W=len(g[0]);V=set();z=[r[:]for r in g]
 for i in range(H*W):
  y,x=divmod(i,W)
  if g[y][x]==0and(y,x)not in V:
   Q=[(y,x)];B={(y,x)};V|={(y,x)}
   while Q:
    r,c=Q.pop(0)
    for d,e in(0,1),(1,0),(0,-1),(-1,0):
     n,m=r+d,c+e
     if H>n>-1<W>m>-1and(n,m)not in V and g[n][m]==0:V|={(n,m)};Q+=[(n,m)];B|={(n,m)}
   Y=[b[0]for b in B];X=[b[1]for b in B];a=min(Y);b=max(Y);c=min(X);d=max(X);h=b-a+1
   if h==d-c+1==len(B)**.5and(a<1or all(g[a-1][x]==5for x in range(c,d+1)))and(b>=H-1or all(g[b+1][x]==5for x in range(c,d+1)))and(c<1or all(g[y][c-1]==5for y in range(a,b+1)))and(d>=W-1or all(g[y][d+1]==5for y in range(a,b+1))):
    for y,x in B:z[y][x]=2
 return z
