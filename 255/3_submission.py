def p(a):
 w=range(31);S=[[0]*31for _ in w]
 for t,u,r in zip(S[1:],S,a):
  for j in w[:30]:t[j+1]=t[j]+u[j+1]-u[j]+(r[j]>0)
 f=lambda y,x,Y,X:S[Y][X]-S[y][X]-S[Y][x]+S[y][x]<1
 b=0
 for y in w[:30]:
  for x in w[:30]:
   for Y in w[y+3:]:
    for X in w[x+3:]:
     if f(y,x,Y,X)*f(y-(y>0),x-(x>0),Y+(Y<30),X+(X<30))*(t:=max(Y-y,X-x)<<10|(Y-y)*(X-x))>b:b=t;A=y;B=x;C=Y;D=X
 for r in a[A:C]:r[B:D]=[3]*(D-B)
 O=[[0]*32]+[[0]+r+[0]for r in a]+[[0]*32]
 for i in w[A:C]:
  for j in w[B:D]:
   for U,V in(1,0),(-1,0),(0,1),(0,-1):
    p=i+U+1;q=j+V+1
    while 0<p<31>q>0==O[p][q]|O[p+V][q+U]|O[p-V][q-U]:p+=U;q+=V
    if{p,q}&{0,31}:
     while(p,q)!=(i+U+1,j+V+1):p-=U;q-=V;a[p-1][q-1]=3
 return a
