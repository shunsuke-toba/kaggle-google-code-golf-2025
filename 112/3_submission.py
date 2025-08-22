def p(j,p=enumerate):
 Y=X=0
 for y,r in p(j):
  for x,l in p(r):Y+=y*(l>2);X+=x*(l>2)
 Y//=2;X//=2
 for y,r in p(j):
  for x,l in p(r):
   if l==2:j[y][x]=j[Y-y][x]=j[y][X-x]=j[Y-y][X-x]=l
 return j