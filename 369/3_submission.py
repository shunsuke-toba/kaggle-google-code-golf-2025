def p(g):
 def f(r,c):
  if 0<=r<10>c>=g[r][c]<1:g[r][c]=4;q[:0]=(r,c),;[f(r+d,c)or f(r,c+d)for d in(-1,1)]
 for n in range(100):
  q=[];f(n//10,n%10)
  for r,c in q:g[r][c]-=len(q)
 return g