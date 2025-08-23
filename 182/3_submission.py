def p(g):
 R=range;r=R(5);n=len(g)-6;m=R(n+2)
 t=next({(i,j)for i in r for j in r if(v:=g[y+i+1][x+j+1])>1and(c:=v)}for y in R(n)for x in R(n)if g[y][x]&g[y][x+1]&g[y+1][x]>4)
 for y in m:
  for x in m:
   if{(i,j)for i in r for j in r if g[y+i][x+j]}==t:
    for i,j in t:g[y+i][x+j]=c
 return g
