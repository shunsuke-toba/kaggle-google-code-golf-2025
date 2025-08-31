def p(g):
 for k,v in enumerate(sum(g,[])):
  if v>4:
   I,J=i,j=k//15,k%15
   while g[i:=i+(I<2)-(I>11)][j:=j+(J<2)-(J>11)]-2:0
   g[I][J]=0;g[i*2-I][j*2-J]=5
 return g