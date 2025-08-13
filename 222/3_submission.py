def p(g):
 R,C=len(g),len(g[0]);o=[[0]*C for _ in range(R)]
 for r in range(R):
  for c in range(C):
   for r2 in range(R-1,r,-1):
    for c2 in range(C-1,c,-1):
     if(r2-r+1)*(c2-c+1)<6:continue
     v=g[r][c]
     if v<1 or any(g[i][j]!=v for i in range(r,r2+1)for j in range(c,c2+1)):continue
     for i in range(r,r2+1):
      for j in range(c,c2+1):o[i][j]=v
     return o