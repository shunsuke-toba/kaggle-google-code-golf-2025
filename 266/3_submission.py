def p(g):
 i=sum(g,[]).index(2);x=i%5
 for d,c in(-6,3),(-4,6),(4,8),(6,7),(0,0):
  if-1<(j:=i+d)<15>-2<j%5-x<2:g[j//5][j%5]=c
 return g
