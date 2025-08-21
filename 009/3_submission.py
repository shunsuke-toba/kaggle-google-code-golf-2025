def p(g):
 b=g[0][2]
 for c in range(20):
  for r in g:
   t=[i for i,x in enumerate(r)if x==(d:=c//2)]
   if d>0<len(t)==4:r[t[1]+1:t[-2]]=[b+(d+10-b)*(r[i]!=b)for i in range(t[1]+1,t[-2])]
  g=[*map(list,zip(*g))]
 return[[x%10for x in r]for r in g]
