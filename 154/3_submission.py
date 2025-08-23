def p(g):
 for i,j in[(i,j)for k in range(225)if g[i:=k//15][j:=k%15]&4]:
  for y,x in(1,0),(-1,0),(0,1),(0,-1):
   d=1
   try:
    while g[i+y*d][j+x*d]-2:d+=1
    g[i][j]=0;g[i+y*d*2][j+x*d*2]=5;break
   except:0
 return g