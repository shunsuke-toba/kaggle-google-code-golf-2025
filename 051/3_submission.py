def p(g):
 for _ in[0]*4:
  for a in g:
   for y,b in enumerate(a[1:]):
    if 2>sum(g,[]).count(a[y])>b:a[:y]=[i or a[y]for i in a[:y]]
  g=[*map(list,zip(*g[::-1]))]
 return g