E=enumerate
def p(g):
 n=len(g);m=n+1
 for y,r in E(g):
  for x,v in E(r):
   if v>8:
    r[x]=min(g[A][B]for Y in (y,m-y) for X in (x,m-x) for A,B in((Y,X),(X,Y))if 0<=A<n> B)
 return g
