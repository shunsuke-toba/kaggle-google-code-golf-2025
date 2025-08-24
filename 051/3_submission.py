def p(g,r=range):
 for _ in[0]*4:
  for a in g:
   for y in r(len(a)-1):
    if sum(g,[]).count(c:=a[y])<2>1>a[y+1]:a[:y]=[a[i]or c for i in r(y)]
  g=[*map(list,zip(*g[::-1]))]
 return g
