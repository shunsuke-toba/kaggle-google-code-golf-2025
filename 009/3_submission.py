def p(g):
 b=g[0][2]
 for c in range(18):
  for r in g:
   t=[i for i,x in enumerate(r)if x==(d:=c//2+1)]
   if len(t)==4:r[t[1]+1:t[-2]]=[b+(d+10-b)*(x!=b)for x in r[t[1]+1:t[-2]]]
  g=[*map(list,zip(*g))]
 return[[x%10for x in r]for r in g]
