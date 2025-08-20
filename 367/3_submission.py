def p(g):
 h,w=len(g),len(g[0]);d=-1,0,1,0
 for k in range(9**5):
  r,c,s=k%97%h,k%89%w,k%4;x,y=d[s],d[~s];t=g[r][c]
  try:g[r+d[s-1]+x-h][c+x+y]|=([g[r+d[s+~i]][c+d[s-i]]for i in range(4)]==[5,0,0,5])*t>4 and 4
  except:0
  if h>r+x>-1<c+y<w>5>t:g[r+x][c+y]|=t
 return g
