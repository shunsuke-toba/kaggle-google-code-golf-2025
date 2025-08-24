def p(g):
 p=range(100)
 for k in p:
  if 7<g[i:=k//10][j:=k%10]:
   c=[(i,j)]
   for i,j in c:
    for s in range(9):
     if-1<(x:=i+s//3-1)<10>(y:=j+s%3-1)>-1<g[x][y]-7:g[x][y]=1;c+=[(x,y)]
   p=min(p,c,key=len)
 for i,j in p:g[i][j]=2
 return g
