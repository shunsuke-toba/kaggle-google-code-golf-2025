def p(g):
 for k,c in enumerate(sum(g,[])):
  if c%8:
   i=k//10;j=k%10
   for a,b in(1,0),(0,1),(-1,0),(0,-1):
    x=i+a;y=j+b
    while 9>=x>=0<=y<=9 and g[x][y]<1:x+=a;y+=b
    try:
     if g[x][y]==8:g[x][y]=c
    except:0
 return g
