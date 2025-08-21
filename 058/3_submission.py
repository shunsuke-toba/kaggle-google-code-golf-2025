def p(g):
 n=len(g);g[0]=[3]*n;x=n-1;y=0;d=1,0,-1,0;i=1
 for n in range(n-1,0,-2):
  for _ in 0,0:
   for _ in[0]*n:y+=d[i-1];x+=d[i];g[y][x]=3
   i=-~i%4
 return g
