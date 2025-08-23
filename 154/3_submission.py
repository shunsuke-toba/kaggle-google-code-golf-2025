def p(g):
 for i,j in[(i,j)for k in range(225)if g[i:=k//15][j:=k%15]>2]:
  for y,x in(1,0),(-1,0),(0,1),(0,-1):
   a,b=i,j
   try:
    while g[a:=a+y][b:=b+x]-2:0
    g[i][j]=0;g[a*2-i][b*2-j]=5;break
   except:0
 return g