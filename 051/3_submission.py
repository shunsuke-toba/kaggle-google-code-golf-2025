def p(g,R=range):
 for _ in[0]*4:
  for x in R(len(g)):
   for y in R(len(g[0])-1):
    if(sum(g,[])).count(c:=g[x][y])<2>1>g[x][y+1]:g[x][:y]=[(d:=g[x][i])+c*(d<1)for i in R(y)]
  g=[*map(list,zip(*g[::-1]))]
 return g