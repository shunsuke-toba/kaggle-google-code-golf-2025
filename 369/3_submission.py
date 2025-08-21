def p(g):
 for n in range(100):
  i,j=divmod(n,10)
  q=[(i,j)]*(g[i][j]<1)
  for x,y in q:
   g[x][y]=1
   for X,Y in(x+1,y),(x-1,y),(x,y+1),(x,y-1):
    9>=X>=0<=Y<=9>g[X][Y]*10 and q.append((X,Y))
  for x,y in q:g[x][y]=4-len(q)
 return g
