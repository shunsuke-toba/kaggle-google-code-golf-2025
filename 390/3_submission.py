def p(g):
 for y,x in[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v>4]:
  m=99
  for a,b in(1,0),(0,1),(-1,0),(0,-1):
   i=y;j=x;d=0
   try:
    while g[i+a][j+b]-2:i+=a;j+=b;d+=1
    i+=a;j+=b;d+=1
    if d<m:m=d;p=i;q=j;A=a;B=b
   except:0
  g[y][x]=0;g[p+A*m][q+B*m]=5
 return g
