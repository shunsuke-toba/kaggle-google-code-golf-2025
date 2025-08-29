def p(g):
 for s in range(8**5):
  try:h,w=len(g),len(g[0]);d=-1,0,1,0;t=g[r:=s%97%h][c:=s%89%w]-5;s%=4;g[x:=d[s]+r][y:=d[~s]+c]|=t&4*(x|y>0);g[x-y+c][x-r+y]|=([g[r+d[s+~i]][c+d[s-i]]for i in range(4)]==[5,t,0,5])*4
  except:0
 return g