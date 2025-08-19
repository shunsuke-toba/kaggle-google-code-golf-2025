def p(g,E=enumerate):
 C=sorted({*sum(g,[])},key=lambda x:-sum(r.count(x)for r in g))
 for _ in [0]*4:
  for r in g:
   a,b=[i for i,x in E(r)if x==C[2]],[i for i,x in E(r)if x==C[1]]
   if a and b and a[0]<b[0]:r[a[0]:b[0]]=[C[2]]*(b[0]-a[0])
  g=[*map(list,zip(*g[::-1]))]
 return g