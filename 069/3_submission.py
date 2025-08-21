def p(g):
 r=range(10);p=[]
 for i in r:
  for j in r:
   if(v:=g[i][j])%8:p+=[(i,j,v)];g[i][j]=0
 i,j,_=p[0];p=[(x-i,y-j,z)for x,y,z in p];o=[[0]*10 for _ in r]
 for i in r:
  for j in r:
   try:
    if all(g[i+x][j+y]==8 for x,y,_ in p):
     for x,y,v in p:o[i+x][j+y]=v;g[i+x][j+y]=0
   except:0
 return o
