def p(g):
 s={(i,j)for i,r in enumerate(g)for j,c in enumerate(r)if c==5}
 def f(s):
  if not s:return 1
  r,c=min(s)
  for *q,k in((0,0,1,0,2,0,2),(0,0,0,1,0,2,2),(0,0,1,0,0,1,1,1,8)):
   q={(r+i,c+j)for i,j in zip(q[::2],q[1::2])}
   if q<=s and f(s-q):
    for r,c in q:g[r][c]=k
    return 1
 f(s)
 return g
