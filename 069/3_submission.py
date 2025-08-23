def p(g):
 r=range(10);p=[]
 for i in r:
  for j in r:
   if(v:=g[i][j])%8:
    if not p:a,b=i,j
    p+=[(i-a,j-b,v)];g[i][j]=0
 for i in r:
  for j in r:
   try:
    if{g[i+x][j+y]for x,y,_ in p}=={8}:
     for x,y,v in p:g[i+x][j+y]=v
   except:0
 return g
