from collections import Counter as C
def p(g):
 R,C=len(g),len(g[0]);F=range;m=x=y=s=t=0
 for a in F(R*C):
  q=g[i:=a//C];j=a%C
  for h in F(3,-~R-i):
   for w in F(3,-~C-j):
    if q[j:j+w]==[q[j]]*w and all(r[j]==q[j] for r in g[i:i+h])*all(z<1 for r in g[i+1:i+h-1]for z in r[j+1:j+w-1])and(A:=h*w)>m:m,x,y,s,t=A,i,j,h,w
 for i in F(-~R-s):
  for j in F(-~C-t):
   if(i^x|j^y)*all(z<1 for r in g[i+1:i+s-1]for z in r[j+1:j+t-1]):
    for h in F(s):g[i+h][j:j+t]=g[x+h][y:y+t]
    return g
