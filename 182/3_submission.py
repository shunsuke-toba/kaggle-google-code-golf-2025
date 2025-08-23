def p(g):
 R=range;r=R(5);m=R(len(g)-4)
 t=next({(i,j)for i in r for j in r if(v:=g[y+i+1][x+j+1])and(c:=v)}for y in m for x in m if g[y][x]&g[y][x+1]&g[y+1][x]>4)
 for y in m:
  for x in m:
   if{(i,j)for i in r for j in r if g[y+i][x+j]}==t:
    for i,j in t:g[y+i][x+j]=c
 return g
