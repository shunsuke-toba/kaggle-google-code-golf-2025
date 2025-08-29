def p(g):
 def f(r,c):
  if 10>r>-1<c<10>g[r][c]<1:
   g[r][c]=5;q.append((r,c))
   for d in-1,1:f(r+d,c);f(r,c+d)
 for n in range(100):
  q=[];f(n//10,n%10)
  for r,c in q:g[r][c]=4-len(q)
 return g