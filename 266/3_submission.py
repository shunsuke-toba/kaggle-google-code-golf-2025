def p(g):
 i=sum(g,[]).index(2)
 for a,b,c in(-1,-1,3),(-1,1,6),(1,-1,8),(1,1,7),(0,0,0):
  y=i//5+a;x=i%5+b
  if-1<y<3>-1<x<5:g[y][x]=c
 return g
