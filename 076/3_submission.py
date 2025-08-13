def p(g):
 import numpy as n
 g=n.array(g);h,w=g.shape;V=[[0]*w for _ in[0]*h];C=[]
 for k in range(h*w):
  i,j=k//w,k%w
  if V[i][j]<1and g[i][j]:
   S=[(i,j)];c=[]
   while S:
    y,x=S.pop()
    if 0<=y<h and 0<=x<w and V[y][x]<1and g[y][x]:V[y][x]=1;c+=[(y,x)];S+=[(y+a,x+b)for a in[-1,0,1]for b in[-1,0,1]]
   C+=[c]
 T=0
 for c in C:
  m=min(p[0]for p in c);M=max(p[0]for p in c);k=min(p[1]for p in c);K=max(p[1]for p in c);B=g[m:-~M,k:-~K];s={g[i,j]for i,j in c}
  if{1,2,3,4}<=s:T=B;break
 if type(T)==int:return g.tolist()
 R=[T]+[n.rot90(T,k=-i)for i in[1,2,3]];F=n.fliplr(T);R+=[F]+[n.rot90(F,k=-i)for i in[1,2,3]];r=g.copy()
 for t in R:
  H,W=t.shape
  for k in range((h+1-H)*(w+1-W)):
   i,j=k//(w+1-W),k%(w+1-W);e=g[i:i+H,j:j+W];a=1
   for m in range(H*W):
    y,x=m//W,m%W
    if t[y,x]in[2,4]:a*=e[y,x]==t[y,x]
   if a:exec("r[i:i+H,j:j+W]=n.where(e,e,t)")
 return r.tolist()
