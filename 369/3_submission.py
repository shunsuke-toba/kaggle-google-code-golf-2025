def p(g):
 for n in range(100):
  for x,y in (q:=[divmod(n,10)]*(g[n//10][n%10]<1)):
   g[x][y]=1;q+=[(a,b)for d in(1,-1)for a,b in((x+d,y),(x,y+d))if 9>=a>=0<=b<=9>g[a][b]*9]
  for x,y in q:g[x][y]=4-len(q)
 return g
