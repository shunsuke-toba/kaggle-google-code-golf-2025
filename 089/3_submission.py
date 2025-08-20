def p(g):
 H,W=len(g),len(g[0]);v=[[0]*W for _ in g];P=[];M=[]
 def f(i,j):
  if min(i,j,H-1-i,W-1-j)<0 or v[i][j]or g[i][j]<1:return[]
  v[i][j]=1;c=[(i,j)]
  for a in-1,0,1:
   for b in-1,0,1:a|b and c.extend(f(i+a,j+b))
  return c
 for i in range(H):
  for j in range(W):
   if (V:=g[i][j])>0>=v[i][j]:
    c=f(i,j)
    if len(c)<2<=(n:=V)<4:M+=[(i,j,n)]
    else:
     I,J=zip(*c);A=min(I);B=min(J);h=max(I)-A+1;w=max(J)-B+1;p=[[0]*w for _ in[0]*h];R=S=0
     for x,y in c:
      a=x-A;b=y-B;p[a][b]=V=g[x][y]
      if V==2:R=a,b
      if V==3:S=a,b
     P+=[(p,R,S,h,w)]
 for i,j,c in M:
  for p,R,S,h,w in P:
   d=c<3;T=(S,R)[d]
   if T:
    a,b=T;o=i-a;u=j-b+(2*b-w+1)*d
    for k in range(h*w):
     x,y=divmod(k,w);V=p[x][y+(w-2*y-1)*d]
     if V:n=o+x;m=u+y;H>n>=0 and W>m>=0 and exec("g[n][m]=V")
    break
 return g
