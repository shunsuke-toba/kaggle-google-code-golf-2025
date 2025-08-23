def p(g):
 m={};e=enumerate;s=sorted
 for y,R in e(g):
  for x,v in e(R):
   try:
    Y,X=m[v];a,b=s((y,Y));c,d=s((x,X))
    for R in g[a:b+1]:R[c:d+1]=[v]*(d-c+1)
   except:
    if v:m[v]=y,x
 return g
