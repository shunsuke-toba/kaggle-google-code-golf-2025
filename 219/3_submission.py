def p(g,R=range):
 i=0;T=10
 while~-any(g[i]):i+=1;f=i
 while any(g[i]):i+=1;a=i-f
 while i<14:
  i+=1;u=a+1
  if~-any(g[i]):continue
  while any(g[i]):i+=1;u-=1
  for x in R(3*u):
   t=x//u;s=x%u+i-a;w=m=s>g[1][3]>a*3>g[7][7]>g[1][4]
   for j in R(a*T):g[12][j%6+4]|=j%2<w;m|=g[s+j//T][j%T]>1>g[f+j//T][j%T-t]<=j%T-t
   if~-m:
    for j in R(a*T):k=j%T;j//=T;g[s+j][k]|=g[f+j][k-t]>1>g[s+j][k]<=k-t
    break
 return g
