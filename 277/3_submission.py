def p(g):
 r=range;m=99;p=[]
 for k in r(100):
  if 7<g[i:=k//10][j:=k%10]:
   c=[(i,j)];g[i][j]=1
   for i,j in c:
    for s in r(9):
     if 0<=(x:=i+s//3-1)<10>(y:=j+s%3-1)>=0<g[x][y]+2>9:g[x][y]=1;c+=[(x,y)]
   if(l:=len(c))<m:m=l;p=c
 for i,j in p:g[i][j]=2
 return g
