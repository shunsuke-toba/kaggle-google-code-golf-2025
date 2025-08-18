def p(G,R=range(5)):
 for y in R:
  for x in R:
   a,b,c,d=G[y][x:x+2]+G[y+1][x:x+2]
   if a*b*c*d:
    for Y,X,v in((y+2,x+2,a),(y-2,x-2,d),(y-2,x+2,c),(y+2,x-2,b)):
     for i in Y,Y+1:
      for j in X,X+1:
       if-1<i<6>j>-1:G[i][j]=v
    return G
