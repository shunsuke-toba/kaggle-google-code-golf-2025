def p(g):
 r=range;n=r(len(g))
 for y in n:
  a=g[y]
  for x in n:
   if a[x]<1 or y*g[y-1][x] or x*a[x-1]:continue
   l=(a+[0]).index(0,x)-x
   for j in g[y+1:y+l-1]:j[x+1:x+l-1]=[2|l%2*5]*(l-2)
 return g
