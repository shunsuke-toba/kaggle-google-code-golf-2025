def p(j,p=enumerate):
 for Y,r in p(j):
  if 3in r:X=r.index(3)*2+1;Y=Y*2+1;break
 for y,r in p(j):
  for x,l in p(r):
   if l==2:r[X-x]=j[Y-y][x]=j[Y-y][X-x]=2
 return j
