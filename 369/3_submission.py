def p(g):
 for n in range(100):
  for x,y in(q:=[(r:=n//10,c:=n%10)][g[r][c]:]):g[x][y]=1;q+=[(a,b)for d in(1,-1)for a,b in((x+d,y),(x,y+d))if 10>a>-1<b<10>g[a][b]<1]
  for x,y in q:g[x][y]=4-len(q)
 return g