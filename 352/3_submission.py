def p(g,L=len):
 h,w=L(g),L(g[0])
 for i in range(h*w*9):
  k=i//9
  n,m=k//w+i%9//3-1,k%w+i%3-1
  if h>n>-1<m<w>1>g[n][m]<2==g[k//w][k%w]:g[n][m]=1
 return g