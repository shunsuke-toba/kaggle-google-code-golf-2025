def p(g):
 r=range;m=1e9;p=[]
 for k in r(100):
  if g[(i:=k//10)][(j:=k%10)]>7:
   c=[(i,j)];g[i][j]=1
   for i,j in c:
    for s in r(9):
     X=i+s//3-1;Y=j+s%3-1
     if 0<=X<10>Y>=0<g[X][Y]+2>9:g[X][Y]=1;c+=[(X,Y)]
   if(l:=len(c))<m:m=l;p=c
 for i,j in p:g[i][j]=2
 return g
