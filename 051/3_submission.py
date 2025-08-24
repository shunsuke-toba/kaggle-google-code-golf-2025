def p(g):
 for _ in[0]*4:
  for a in g:
   for y in range(len(a)-1):
    if sum(g,[]).count(a[y])<2>1>a[y+1]:a[:y]=[i or a[y]for i in a[:y]]
  g=[*map(list,zip(*g[::-1]))]
 return g
