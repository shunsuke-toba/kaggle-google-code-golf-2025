def p(g):
 h,w=len(g),len(g[0]);d=-1,0,1,0
 for k in range(9**5):
  r,c,s=k%97%h,k%89%w,k%4;x,y=d[s]+r,d[~s]+c;t=g[r][c];g[(x-y+c)%h][(x-r+y)%w]|=([g[(r+d[s+~i])%h][(c+d[s-i])%w]for i in range(4)]==[5,t-5,0,5])*4
  if h>x>-1<y<w>5>t:g[x][y]|=t
 return g