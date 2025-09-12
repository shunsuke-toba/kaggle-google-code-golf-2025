def p(g):
 w=len(g[0])
 def f(y,x):c=[(y,x,g[y][x])];g[y][x]=0;[c:=c+f(Y,X)for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1))if w>X>-1<Y<len(g)>g[Y][X]>0];return c
 Y,X,p=min(B:=min(C:=[f(i//w,i%w)for i,c in enumerate(sum(g,[]))if c],key=lambda c:(len(c)<3,len(c))),key=lambda t:sum(c==t[2]for*_,c in B))
 for c in C:
  A=[(y,x)for y,x,t in c if t==p or(q:=t)*0]
  for y,x,t in B:
   for i,j in A:g[(y-Y)*int(len(A)**.5)+i][(x-X)*int(len(A)**.5)+j]=(p,q)[t!=p]
 return g