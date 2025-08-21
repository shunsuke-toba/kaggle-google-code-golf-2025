def p(g):
 w=h=len(g)
 def f(i,j):
  if not(h>i>=0<=j<w)or g[i][j]-1:return[]
  g[i][j]=0;return[(i,j)]+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)
 for k in range(h*w):
  if c:=f(k//w,k%w):
   y,x=zip(*c);a,b=min(y),max(y);d,e=min(x),max(x);t=1+2*(len(c)==2*(b-a+e-d)and b-a>1<e-d)
   for y,x in c:g[y][x]=t
 return g
