def p(g):
 for k,v in enumerate(sum(g,[])):
  if v>4:
   a,b=i,j=k//15,k%15;y=(i<2)-(i>11);x=(j<2)-(j>11)
   while g[a:=a+y][b:=b+x]-2:0
   g[i][j]=0;g[a*2-i][b*2-j]=5
 return g