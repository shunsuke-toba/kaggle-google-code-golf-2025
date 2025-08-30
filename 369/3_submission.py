def p(g):
 def f(r,c):
  if 0<=r<10>c>=0==g[r][c]:
   g[r][c]=4;q[:0]=[(r,c)]
   for d in-1,1:f(r+d,c);f(r,c+d)
 for n in range(100):
  q=[];f(n//10,n%10)
  for r,c in q:g[r][c]-=len(q)
 return g