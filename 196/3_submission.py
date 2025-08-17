def p(g):
 R=range;h=len(g);w=len(g[0]);v=set()
 def f(i,j):
  if(i,j)in v or not(h>i>=0<=j<w)or g[i][j]-1:return[]
  v.add((i,j))
  return[(i,j)]+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)
 for k in R(h*w):
  i,j=divmod(k,w)
  if c:=f(i,j):
   Y,X=zip(*c);a,b=min(Y),max(Y);d,e=min(X),max(X)
   if len(c)==2*(b-a+e-d)and b-a>1<e-d:
    for y,x in c:g[y][x]=3
 return g
