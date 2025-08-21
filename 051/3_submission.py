def p(g,R=range):
 for _ in[0]*4:
  s=sum(g,[])
  for r in g:
   for y in R(len(r)-1):
    if s.count(c:=r[y])<2>1>r[y+1]:r[:y]=[(d:=r[i])or c for i in R(y)]
  g=[*map(list,zip(*g[::-1]))]
 return g
