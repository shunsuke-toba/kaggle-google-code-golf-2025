def p(a):
 R=range;S=[[0]*31for _ in[0]*31]
 for i in R(30):
  t,u,r=S[i+1],S[i],a[i]
  for j in R(30):t[j+1]=t[j]+u[j+1]-u[j]+(r[j]>0)
 f=lambda y,x,Y,X:S[Y][X]-S[y][X]-S[Y][x]+S[y][x]<1
 b=-1
 for y in R(30):
  for x in R(30):
   for Y in R(y+3,31):
    for X in R(x+3,31):
     if f(y,x,Y,X)and f(y and y-1,x and x-1,min(Y+1,30),min(X+1,30)):
      H=Y-y;W=X-x;t=max(H,W)<<10|H*W
      if t>b:b=t;B=y,x,Y,X
 y,x,Y,X=B;W=X-x
 for i in R(y,Y):a[i][x:X]=[3]*W
 O=[32*[0]]+[[0]+r[:]+[0]for r in a]+[32*[0]]
 for i in R(y,Y):
  for j in R(x,X):
   I=i+1;J=j+1
   for U,V in((1,0),(-1,0),(0,1),(0,-1)):
    p=I+U;q=J+V
    while 0<p<31>q>0and O[p][q]==O[p+V][q+U]==O[p-V][q-U]==0:p+=U;q+=V
    if 0 in(p,q)or 31 in(p,q):
     while (p,q)!=(I+U,J+V):p-=U;q-=V;a[p-1][q-1]=3
 return a
