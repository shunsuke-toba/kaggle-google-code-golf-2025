def p(G,R=range(5)):
 for y in R:
  for x in R:
   if G[y][x]:
    for a,b,v in zip((2,2,-2,-2),(2,-2,2,-2),G[y][x:x+2]+G[y+1][x:x+2]):
     for i in y+a,y+a+1:
      for j in x+b,x+b+1:
       if-1<i<6>j>-1:G[i][j]=v
    return G
