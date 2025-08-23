def p(g):
 h,w=len(g),len(g[0]);d=-1,0,1,0
 for k in range(9**5):
  r,c,s=k%97%h,k%89%w,k%4;x,y=d[s]+r,d[~s]+c;t=g[r][c]-5;g[(x-y+c)%h][(x-r+y)%w]|=([g[(r+d[s+~i])%h][(c+d[s-i])%w]for i in range(4)]==[5,t,0,5])*4
  if h>x>t<y<w:g[x][y]|=4&t
 return g