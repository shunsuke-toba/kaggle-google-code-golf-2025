def p(g):
 E=enumerate
 for y,x in[(y,x)for y,r in E(g)for x,v in E(r)if v>4]:
  m=9
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   try:
    d=1
    while g[y+a*d][x+b*d]-2:d+=1
    if d<m:m,P,Q=d,y+2*a*d,x+2*b*d
   except:0
  g[y][x]=0;g[P][Q]=5
 return g
