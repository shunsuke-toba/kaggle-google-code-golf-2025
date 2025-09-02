def p(g):
 r=range;l=len;w=l(g[0])
 def f(y,x):c=[(y,x,g[y][x])];g[y][x]=0;[c:=c+f(Y,X)for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1))if w>X>-1<Y<l(g)and g[Y][X]];return c
 Y,X,p=min(B:=min(C:=[f(i//w,i%w)for i in r(w*l(g))if g[i//w][i%w]],key=lambda c:(l(c)<3,l(c))),key=lambda t:sum(c==t[2]for*_,c in B))
 for c in C:
  a,b=min(A:=[(y,x)for y,x,t in c if t==p or(q:=t)*0]);m=int(l(A)**.5)
  for y,x,t in B:
   for i in r(m*m):g[a+(y-Y)*m+i//m][b+(x-X)*m+i%m]=(p,q)[t!=p]
 return g