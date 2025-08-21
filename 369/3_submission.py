def p(g):
 for n in range(100):
  q=[divmod(n,10)]*(g[n//10][n%10]<1)
  for x,y in q:
   g[x][y]=1
   for a,b in(x+1,y),(x-1,y),(x,y+1),(x,y-1):9>=a>=0<=b<=9>g[a][b]*9 and q.append((a,b))
  for x,y in q:g[x][y]=4-len(q)
 return g
