def p(g):
 import numpy as n
 g=n.array(g);h,w=g.shape;a=g.copy();C=[]
 for y in range(h):
  for x in range(w):
   if a[y,x]:
    S=[(y,x)];a[y,x]=0;c=[]
    while S:
     i,j=S.pop();c+=i,j,
     for Y in range(i-1,i+2):
      for X in range(j-1,j+2):
       if 0<=Y<h and 0<=X<w and a[Y,X]:a[Y,X]=0;S.append((Y,X))
    C+=c,
 b=max(C,key=len);T=g[min(b[::2]):max(b[::2])+1,min(b[1::2]):max(b[1::2])+1];R=[]
 for t in T,n.fliplr(T):
  for k in 0,1,2,3:R+=n.rot90(t,k),
 for t in R:
  H,W=t.shape
  for y in range(h-H+1):
   for x in range(w-W+1):
    e=g[y:y+H,x:x+W];m=(t==2)|(t==4)
    if (e[m]==t[m]).all():z=(e==0)&(t>0);e[z]=t[z]
 return g.tolist()
