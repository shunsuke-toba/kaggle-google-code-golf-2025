def p(g):
 r=range;l=len;h=l(g);w=l(g[0])
 def f(y,x):c=[(y,x,g[y][x])];g[y][x]=0;[c:=c+f(Y,X)for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1))if h>Y>=0<=X<w and g[Y][X]];return c
 C=[f(y,x)for y in r(h)for x in r(w)if g[y][x]];B=min(C,key=lambda c:(l(c)<3,l(c)));Y,X,p=min(B,key=lambda t:sum(v[2]==t[2]for v in B))
 for c in C:
  m=int(l(A:=[v for v in c if v[2]==p])**.5);a,b,_=min(A)
  for y,x,t in B:
   for i in r(m):o=b+(x-X)*m;g[a+(y-Y)*m+i][o:o+m]=[[p,sum({v[2]for v in c})-p][t!=p]]*m
 return g