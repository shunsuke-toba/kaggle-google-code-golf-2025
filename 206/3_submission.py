def p(g):
 s=t=a=b=99
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==5:s,t=i,j
   elif v%5:a,b=min(a,i),min(b,j)
 for k in 0,1,2:g[s+k-1][t-1:t+2]=g[a+k][b:b+3]
 return g
