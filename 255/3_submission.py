def p(a):
 R=range;S=[[0]*31for _ in R(31)]
 for t,u,r in zip(S[1:],S,a):
  for j in R(30):t[j+1]=t[j]+u[j+1]-u[j]+(r[j]>0)
 f=lambda y,x,Y,X:S[Y][X]-S[y][X]-S[Y][x]+S[y][x]<1
 b=0
 for y in R(30):
  for x in R(30):
   for Y in R(y+3,31):
    for X in R(x+3,31):
     if f(y,x,Y,X)*f(y-(y>0),x-(x>0),Y+(Y<30),X+(X<30))*(t:=max(Y-y,X-x)<<10|(Y-y)*(X-x))>b:b=t;B=y,x,Y,X
 y,x,Y,X=B
 for r in a[y:Y]:r[x:X]=[3]*(X-x)
 O=[32*[0]]+[[0]+r*1+[0]for r in a]+[32*[0]]
 for i in R(y,Y):
  for j in R(x,X):
   for U,V in(1,0),(-1,0),(0,1),(0,-1):
    p=i+U+1;q=j+V+1
    while 0<p<31>q>0==O[p][q]|O[p+V][q+U]|O[p-V][q-U]:p+=U;q+=V
    if{p,q}&{0,31}:
     while (p,q)!=(i+U+1,j+V+1):p-=U;q-=V;a[p-1][q-1]=3
 return a
