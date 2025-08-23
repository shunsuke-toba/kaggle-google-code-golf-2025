def p(g):
 w=len(g)
 def f(i,j):
  if not(w>i>=0<=j<w)or g[i][j]-1:return[]
  g[i][j]=0;return[(i,j)]+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)
 for k in range(w*w):
  if c:=f(k//w,k%w):
   h,l=[max(t)-min(t)for t in zip(*c)]
   for y,x in c:g[y][x]=1+2*(len(c)/2==h+l and h>1<l)
 return g