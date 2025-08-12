def p(g):
 g=[r[:]for r in g];h,w=len(g),len(g[0])
 c={(y,x)for y in range(h)for x in range(w)if g[y][x]==8}
 for y in range(h):
  for x in range(w):
   v=g[y][x]
   if v and v-8:
    b=min(((abs(j-x)if i==y else abs(i-y)if j==x else 999,i,j)for i,j in c),default=(999,0,0))
    if b[0]<999:g[b[1]][b[2]]=v
 return g