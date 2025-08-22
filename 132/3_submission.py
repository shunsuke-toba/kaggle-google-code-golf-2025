def p(g):
 m={};e=enumerate;s=sorted
 for y,R in e(g):
  for x,v in e(R):
   if v:
    try:
     Y,X=m[v];a,b=s((y,Y));c,d=s((x,X))
     for Y in range(a,b+1):g[Y][c:d+1]=[v]*(d-c+1)
    except:m[v]=(y,x)
 return g
