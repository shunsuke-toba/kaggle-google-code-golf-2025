def p(g):
 s=t=a=b=9;e=enumerate
 for i,r in e(g):
  for j,v in e(r):
   if v==5:s,t=i,j
   if v%5:a,b=min(a,i),min(b,j)
 for k in 0,1,2:g[s+k-1][t-1:t+2]=g[a+k][b:b+3]
 return g
