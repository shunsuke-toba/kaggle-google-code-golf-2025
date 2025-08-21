def p(g,r=range):
 c=len(g)
 for q in r(c*c):
  y=q//c;x=q%c
  if g[y][x]%5:
   Y,X=y,x;h=w=1
   while y+h<c and g[y+h][x]%5:h+=1
   while x+w<c and g[y][x+w]%5:w+=1
   break
 for y in r(c-h+1):
  for x in r(c-w+1):
   if g[y][x]==5:
    for q in r(h):g[y+q][x:x+w]=g[Y+q][X:X+w]
 return g
