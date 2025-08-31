def p(g):
 for k,v in enumerate(sum(g,[])):
  if v>4:
   I=i=k//15;J=j=k%15
   while g[i:=i+(I<2)-I//12][j:=j+(J<2)-J//12]-2:0
   g[I][J]=0;g[i*2-I][j*2-J]=v
 return g