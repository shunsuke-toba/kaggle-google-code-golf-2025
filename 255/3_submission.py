def p(g):
 w=range(31);v=w[:30];s=[[0]*31 for _ in w]
 for t,u,r in zip(s[1:],s,g):
  for j in v:t[j+1]=t[j]+u[j+1]-u[j]+(r[j]>0)
 f=lambda a,b,c,d:s[c][d]-s[a][d]-s[c][b]+s[a][b]<1;b=0
 for y in v:
  for x in v:
   for Y in w[y+3:]:
    for X in w[x+3:]:
     if f(y,x,Y,X)*f(y-(y>0),x-(x>0),Y+(Y<30),X+(X<30))*(t:=max(h:=Y-y,W:=X-x)<<10|h*W)>b:b=t;A=y;B=x;C=Y;D=X
 for r in g[A:C]:r[B:D]=[3]*(D-B)
 o=[[0]*32]+[[0,*r,0]for r in g]+[[0]*32]
 for i in w[A:C]:
  for j in w[B:D]:
   for U,V in(1,0),(-1,0),(0,1),(0,-1):
    p=i+U+1;q=j+V+1
    while 0<p<31>q>0==o[p][q]|o[p+V][q+U]|o[p-V][q-U]:p+=U;q+=V
    if{p,q}&{0,31}:
     while(p,q)!=(i+U+1,j+V+1):p-=U;q-=V;g[p-1][q-1]=3
 return g
