def p(g):
 s={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v}
 def f(s):
  if not s:return 1
  r,c=min(s)
  for d,v in(((0,0,0,1,1,0,1,1),8),((0,0,0,1,0,2,0,2),2),((0,0,1,0,2,0,2,0),2)):
   t={(r+d[i],c+d[i+1])for i in(0,2,4,6)}
   if t<=s:
    for a,b in t:g[a][b]=v
    if f(s-t):return 1
    for a,b in t:g[a][b]=5
  return 0
 if not f(s):
  for a,b in s:g[a][b]=8
 return g
