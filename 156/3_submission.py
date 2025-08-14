def p(g):
 t=[]
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v>3and(y<1or g[y-1][x]^4)and(x<1or r[x-1]^4):
    X=x;Y=y
    while X<len(r)and r[X]==4:X+=1
    while Y<len(g)and g[Y][x]==4:Y+=1
    t+=((Y-y)*(X-x),y,x,Y,X),
 for(a,y,x,Y,X),c in zip(sorted(t),(1,2)):
  for y in range(y+1,Y-1):g[y][x+1:X-1]=[c]*(X-x-2)
 return g
