def p(g):
 h=len(g);w=len(g[0]);z=[*map(list,g)]
 for t in range(h*w):
  y,x=divmod(t,w)
  if f:=g[y][x]:
   a=b=y;d=e=x;Q=[(y,x)];g[y][x]=0
   for r,j in Q:
    for nr,nc in((r+1,j),(r-1,j),(r,j+1),(r,j-1)):
     if h>nr>=0<w>nc>=0 and g[nr][nc]==f:g[nr][nc]=0;Q+=(nr,nc),;a=min(a,nr);b=max(b,nr);d=min(d,nc);e=max(e,nc)
   if (n:=b-a+1)==e-d+1>2:
    i=g[a+1][d+1]
    for k in range(1,n//2+1):
     for j in range(d,e+1):
      a>=k and exec("z[a-k][j]=f");b+k<h and exec("z[b+k][j]=f")
     for r in range(a,b+1):
      d>=k and exec("z[r][d-k]=f");e+k<w and exec("z[r][e+k]=f")
    for m in range((b-a+1)*(e-d+1)):
     r,j=divmod(m,e-d+1);r+=a;j+=d;t=z[r][j];z[r][j]=[t,i,f][(t==f)+(t==i)*2];g[r][j]=0
 return z
