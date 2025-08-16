def p(g):
 m=n=99
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:m=min(m,i);n=min(n,j)
 r=range(5)
 a=[g[m+i][n:n+5]for i in r]
 for _ in[0]*3:a=[[a[i][j]or a[4-j][i]for j in r]for i in r]
 for i in r:g[m+i][n:n+5]=a[i]
 return g
