def p(g):
 H,W=len(g),len(g[0]);v=[[0]*W for _ in[0]*H];P=[];M=[]
 def f(i,j):
  if min(i,j)<0 or i>=H or j>=W or v[i][j]or g[i][j]<1:return[]
  v[i][j]=1;c=[(i,j)]
  for a in-1,0,1:
   for b in-1,0,1:a|b and c.extend(f(i+a,j+b))
  return c
 for k in range(H*W):
  i,j=divmod(k,W)
  if v[i][j]<1 and g[i][j]:
   c=f(i,j);l=len(c)
   if l==1:g[i][j]in[2,3]and M.append((i,j,g[i][j]))
   elif l>1:
    I=[x[0]for x in c];J=[x[1]for x in c];h=max(I)-min(I)+1;w=max(J)-min(J)+1;p=[[0]*w for _ in[0]*h];r=s=R=S=0
    for x,y in c:
     p[x-min(I)][y-min(J)]=V=g[x][y]
     if V==2:r=1;R=x-min(I),y-min(J)
     if V==3:s=1;S=x-min(I),y-min(J)
    P+=[(p,r,s,R,S)]
 r=[x[:]for x in g]
 for i,j,c in M:
  for p,q,t,R,S in P:
   if c==2 and q and R:
    h=len(p);w=len(p[0]);a,b=R;b=w+~b;o=i-a;u=j-b
    for k in range(h*w):
     x,y=divmod(k,w);V=p[x][w+~y]
     if V:n=o+x;m=u+y;0<=n<H and 0<=m<W and exec("r[n][m]=V")
    break
   elif c==3 and t and S:
    h=len(p);w=len(p[0]);a,b=S;o=i-a;u=j-b
    for k in range(h*w):
     x,y=divmod(k,w);V=p[x][y]
     if V:n=o+x;m=u+y;0<=n<H and 0<=m<W and exec("r[n][m]=V")
    break
 return r
