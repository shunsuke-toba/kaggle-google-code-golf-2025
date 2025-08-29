def p(g):
 for s in range(8**5):
  try:d=-1,0,1,0;t=g[r:=s%97%len(g)][c:=s%89%len(g[0])]-5;s%=4;g[x:=d[s]+r][y:=d[~s]+c]|=t&4*(x|y>0);g[x-y+c][x-r+y]|=([g[r+d[s+~i]][c+d[s-i]]for i in range(4)]==[5,t,0,5])*4
  except:0
 return g