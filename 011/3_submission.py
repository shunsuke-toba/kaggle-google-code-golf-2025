def p(g):
 for i in 0,4,8:
  for j in 0,4,8:
   if 8 not in sum([r[j:j+3]for r in g[i:i+3]],[]):R=range(11);return[[5*(x%4>2 or y%4>2)or g[i+x//4][j+y//4]for y in R]for x in R]
