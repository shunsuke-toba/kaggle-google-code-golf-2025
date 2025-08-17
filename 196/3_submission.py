def p(g):
 h=len(g);w=len(g[0])
 def f(i,j):
  if not(h>i>=0<=j<w)or g[i][j]-1:return[]
  g[i][j]=0
  return[(i,j)]+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)
 for k in range(h*w):
  i=k//w;j=k%w
  if c:=f(i,j):
   Y,X=zip(*c);a,b=min(Y),max(Y);d,e=min(X),max(X);t=1
   if len(c)==2*(b-a+e-d)and b-a>1<e-d:t=3
   for y,x in c:g[y][x]=t
 return g
