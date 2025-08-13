def p(g):
 m=r=c=h=w=0;R=len(g);C=len(g[0])
 for r1 in range(R):
  for c1 in range(C):
   for r2 in range(r1+2,R):
    for c2 in range(c1+2,C):
     if all(g[x][c1]==g[r1][c1]for x in range(r1,r2+1))&all(g[r1][y]==g[r1][c1]for y in range(c1,c2+1))&all(g[x][y]==0for x in range(r1+1,r2)for y in range(c1+1,c2)):
      a=(r2-r1+1)*(c2-c1+1)
      if a>m:m,r,c,h,w=a,r1,c1,r2-r1+1,c2-c1+1
 for r1 in range(R-h+1):
  for c1 in range(C-w+1):
   if all(g[x][y]==0for x in range(r1+1,r1+h-1)for y in range(c1+1,c1+w-1)):
    for i in range(h):
     for j in range(w):g[r1+i][c1+j]=g[r+i][c+j]
 return g