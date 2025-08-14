def p(g):
 r=[*map(list,g)];B=[(y,x)for y,R in enumerate(g)for x,v in enumerate(R)if v]
 if B:
  y,x=zip(*B);a=min(y);b=max(y);c=min(x);d=max(x)
  for i in range(c,d+1):r[a][i]=r[a][i]or 2;r[b][i]=r[b][i]or 2
  for i in range(a,b+1):r[i][c]=r[i][c]or 2;r[i][d]=r[i][d]or 2
  L=[(0,y,sum(g[y][c+1:d]))for y in range(a+1,b)]+[(1,x,sum(g[y][x]for y in range(a+1,b)))for x in range(c+1,d)]
  m=L and max(l[2]for l in L)
  if m:
   for t,p,n in L:
    if n==m:
     for i in range((a,c)[t<1],(b+1,d+1)[t<1]):j=(p,i)[t>0];k=(i,p)[t>0];r[j][k]=r[j][k]or 2
 return r
