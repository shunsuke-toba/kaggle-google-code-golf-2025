def p(g,R=range):
 i=a=0;T=10
 while~-any(g[i]):i+=1
 f=i
 while any(g[i]):a+=1;i+=1
 while i<14:
  i+=1
  if~-any(g[i]):continue
  s=i;n=0
  while any(g[i]):n+=1;i+=1
  M=0
  for t in R(3):
   for S in R(s-a+n,s+1):
    m=1
    if S>g[1][3]>a*3>g[7][7]>g[1][4]:g[12][4]=g[12][6]=g[12][8]=1;m=0
    for j in R(a*T):
     if g[S+j//T][j%T]>1>g[f+j//T][j%T-t]<=j%T-t:m=0
    if m:
     for j in R(a*T):k=j%T;j//=T;g[S+j][k]|=g[f+j][k-t]>1>g[S+j][k]<=k-t;M=1
     break
   if M:break
 return g
