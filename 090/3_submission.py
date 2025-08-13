def p(g):
 H,W=len(g),len(g[0]);m=0;B=0
 for i in range(H):
  for j in range(W):
   if g[i][j]<1:
    for r in range(i+1,H):
     for c in range(j+1,W):
      h=r-i+1;w=c-j+1
      if h>1 and w>1:
       v=all(g[y][x]<1 for y in range(i,r+1)for x in range(j,c+1))
       if v and h*w>m:m=h*w;B=i,j,r,c
 r=[x[:]for x in g]
 if B:
  i,j,u,v=B
  for y in range(i,u+1):
   for x in range(j,v+1):r[y][x]=6
 return r
