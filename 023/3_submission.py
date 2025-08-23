def p(g):
 s={(i,j)for i,r in enumerate(g)for j,c in enumerate(r)if c}
 def f(s):
  if not s:return 1
  r,c=min(s)
  for *q,k in((0,20,40,2),(0,1,2,2),(0,20,1,21,8)):
   q={(r+d//20,c+d%20)for d in q}
   if q<=s and f(s-q):
    for r,c in q:g[r][c]=k
    return 1
 f(s)
 return g
