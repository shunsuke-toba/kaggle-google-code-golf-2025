def p(g):
 for i,j in[(k//15,k%15)for k in range(225)if g[k//15][k%15]>4]:
  y=(i<2)-(i>11);x=(j<2)-(j>11);a,b=i,j
  while g[a:=a+y][b:=b+x]-2:0
  g[i][j]=0;g[a*2-i][b*2-j]=5
 return g