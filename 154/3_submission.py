def p(g):
 h=eval(str(g))
 for k in range(225):
  i=k//15;j=k%15
  for y,x in((1,0),(-1,0),(0,1),(0,-1))*(g[i][j]>4):
   d=1
   try:
    while g[i+y*d][j+x*d]^2:d+=1
    h[i][j]=0;h[i+y*d*2][j+x*d*2]=5;break
   except:0
 return h