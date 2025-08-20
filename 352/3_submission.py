def p(g):
 for i in range(9**5):
  h,w=len(g),len(g[0]);n,m,x,y=i%97%h,i%87%w,i%83%3-1,i%79%3-1
  if h>n+x>-1<m+y<w>2==g[n+x][m+y]>g[n][m]:g[n][m]=1
 return g