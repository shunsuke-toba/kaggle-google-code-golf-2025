def p(g):
 w=len(g)
 def f(i,j):
  if not(w>i>=0<=j<w)or g[i][j]-1:return[]
  g[i][j]=0;return[(i,j)]+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1)
 for k in range(w*w):
  if c:=f(k//w,k%w):
   y,x=zip(*c);a,b,d,e=min(y),max(y),min(x),max(x)
   for y,x in c:g[y][x]=1+2*(len(c)==2*(b-a+e-d)and b-a>1<e-d)
 return g
