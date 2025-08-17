def p(g):
 import numpy as n
 g=n.array(g);h,w=g.shape;a=g.copy()
 y,x=n.argwhere(g%2)[0]
 S=[(y,x)];a[y,x]=0;b=[]
 while S:
  i,j=S.pop();b+=i,j,
  for Y in range(i-1,i+2):
   for X in range(j-1,j+2):
    if 0<=Y<h and 0<=X<w and a[Y,X]:a[Y,X]=0;S.append((Y,X))
 T=g[min(b[::2]):max(b[::2])+1,min(b[1::2]):max(b[1::2])+1]
 for t in T,n.fliplr(T):
  for k in 0,1,2,3:
   s=n.rot90(t,k);H,W=s.shape
   for y in range(h-H+1):
    for x in range(w-W+1):
     e=g[y:y+H,x:x+W];m=(s==2)|(s==4)
     if (e[m]==s[m]).all():z=(e==0)&(s>0);e[z]=s[z]
 return g.tolist()
