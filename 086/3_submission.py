def p(g):
 H=len(g);W=H and len(g[0]);c={*sum(g,[])}-{0};z=[x[:]for x in g];S=[];V={}
 if len(c)<2:return g
 for f in c:
  for k in range(H*W):
   y,x=divmod(k,W)
   if(y,x)in V or g[y][x]-f:continue
   a=b=y;d=e=x;Q=[(y,x)];C={(y,x)}
   while Q:
    r,j=Q.pop(0)
    for o,p in(0,1),(1,0),(0,-1),(-1,0):
     nr,nc=r+o,j+p
     if H>nr>-1<W>nc>-1and(nr,nc)not in C and g[nr][nc]==f:C.add((nr,nc));Q+=[(nr,nc)];a=min(a,nr);b=max(b,nr);d=min(d,nc);e=max(e,nc)
   h=b-a+1
   if h==e-d+1>2:
    i=0
    for m in range((b-a)*(e-d)):
     r,j=divmod(m,e-d);r+=a+1;j+=d+1
     if g[r][j]-f:i=g[r][j];break
    if i:
     S+=[(f,i,a,b,d,e,h)]
     for m in range(h*(e-d+1)):r,j=divmod(m,e-d+1);V[a+r,d+j]=1
 for f,i,a,b,d,e,n in S:
  x=n//2
  for k in range(1,x+1):
   for j in range(d,e+1):
    a>k-1and exec("z[a-k][j]=f");b+k<H and exec("z[b+k][j]=f")
   for r in range(a,b+1):
    d>k-1and exec("z[r][d-k]=f");e+k<W and exec("z[r][e+k]=f")
  for m in range((b-a+1)*(e-d+1)):r,j=divmod(m,e-d+1);r+=a;j+=d;z[r][j]=[z[r][j],i,f][(g[r][j]==f)+(g[r][j]==i)*2]
 return z
