def p(g,R=range(6)):
 for y in R:
  for x in R:
   if(l:=g[y][x:x+2]+g[y+1][x:x+2]).count(8)>2:g[y+(i:=l.index(0))//2][x+i%2]=1
 return g
