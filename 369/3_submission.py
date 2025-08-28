def p(g):
 def f(r,c):
  if 10>r>-1<c<10>g[r][c]<1:
   g[r][c]=5;q.append((r,c));f(r+1,c);f(r-1,c);f(r,c+1);f(r,c-1)
 for n in range(100):
  q=[];f(*divmod(n,10))
  for r,c in q:g[r][c]=4-len(q)
 return g